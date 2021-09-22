import socket
import pickle
import psutil,time
from CONSTANTES import *
from funcoes import formata_tamanho

PORTA = PORTA + 1

def retorna_memoria():
    memoria = psutil.virtual_memory()
    percent_uso = round(((memoria.used / memoria.total) * 100), 2)
    memoria_json = {
        "Total": formata_tamanho(memoria.total)
        , "Em uso": formata_tamanho(memoria.used)
        , "percent_uso": memoria.percent
        , "Livre": formata_tamanho(memoria.free)
        , "percent_livre": round(100 - percent_uso, 2)
    }
    return memoria_json


udp = socket.socket (socket.AF_INET, socket.SOCK_DGRAM)
udp.bind((HOST, PORTA))

while True:
    print(f"Esperando receber conexão {HOST} na porta {PORTA}")

    (msg, cliente) = udp.recvfrom(1024)
    msg = msg.decode('utf-8')

    if msg == MSG_INICIO:
        time.sleep(5)
        resposta = retorna_memoria()
        bytes_resp = pickle.dumps(resposta)

        udp.sendto(bytes_resp,cliente)

udp.close()
