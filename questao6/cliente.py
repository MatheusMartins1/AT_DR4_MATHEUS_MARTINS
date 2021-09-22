import json
import socket
import pickle
from CONSTANTES import HOST,PORTA
from questao3 import valida_diretorio

def q6_cliente(diretorio):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    resposta = ""
    caminho = valida_diretorio(diretorio)
    try:
        print(f"\nSocket conectando ao servidor em {HOST}:{PORTA}")
        s.connect((HOST, PORTA))

        s.send(caminho.encode('utf-8'))

        bytes = s.recv(4096)

        resposta = pickle.loads(bytes, fix_imports=True, encoding="utf-8")

    except Exception as erro:
        print("erro:",str(erro))

    print("fim conexão socket\n")
    s.close()

    return resposta

resp = q6_cliente("")
print("Arquivos recebidos do cliente:\n",json.dumps(resp, indent=4))