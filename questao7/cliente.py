import socket
import pickle
import time
import json
from CONSTANTES import *

PORTA = PORTA + 1

def q8_cliente():
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp.settimeout(5)
    dest = (HOST, PORTA)

    print(f"Realizando conexão {HOST} na porta {PORTA}")
    udp.sendto(MSG_INICIO.encode("utf-8"),dest)
    recebido = False

    print(f"Enviando requisição 1/6 - Tempo:{time.strftime('%H:%M:%S', time.localtime())}")
    try:
        (resposta, servidor) = udp.recvfrom(4096)
        recebido = True
    except socket.timeout:
        udp.sendto(MSG_INICIO.encode("utf-8"), dest)
        print(f"Enviando requisição 2/6 - Tempo:{time.strftime('%H:%M:%S', time.localtime())}")

        for i in range(1, 5):
            if not recebido:
                try:
                    (resposta, servidor) = udp.recvfrom(4096)
                    recebido = True
                    print(f"Dados retornados")
                except socket.timeout:
                    udp.sendto(MSG_INICIO.encode("utf-8"),dest)
                    print(f"Enviando requisição {i+2}/6 - Tempo:{time.strftime('%H:%M:%S', time.localtime())}")

    udp.close()

    if recebido:
        disco_json = pickle.loads(resposta, fix_imports=True, encoding="utf-8")
        disco_json['hora'] = time.strftime('%d/%m/%y %H:%M:%S',time.localtime())

        print(json.dumps(disco_json, indent=4, sort_keys=True), '\n')
        return disco_json

    else:
        print("Não foi possível recuperar os dados")
        return None


q8_cliente()