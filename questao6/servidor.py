import socket
import pickle
from CONSTANTES import HOST,PORTA
from questao3 import q3

def q6_server():
    # Cria o socket
    socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_servidor.bind((HOST, PORTA))
    socket_servidor.listen()

    while True:
        try:
            print("Servidor de nome", HOST, "esperando conexão na porta", PORTA)
            resposta = False
            (socket_cliente, addr) = socket_servidor.accept()
            print("\nConectado a:", socket_cliente, str(addr))

            msg = socket_cliente.recv(1024)
            msg = msg.decode('utf-8')

            resposta = q3(msg)

            if resposta:
                # Prepara a lista para o envio
                bytes_resp = pickle.dumps(resposta)

                # Envia os dados
                socket_cliente.send(bytes_resp)
                print("enviado")

            while msg == "fim":
                # socket_cliente.send(resp.encode('utf-8'))
                socket_cliente.close()

        except Exception as e:
            print(e)


q6_server()