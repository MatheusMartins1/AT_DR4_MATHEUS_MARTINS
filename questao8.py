# Dado um vetor A de tamanho N com apenas números inteiros positivos, calcule o fatorial de cada um deles e armazene o resultado em um vetor B.
# Para calcular o fatorial, utilize a seguinte função:
import time
from random import randint,random

tamanho = 10
vetor_b_tread = []

def gera_vetor(tamanho):
    vertorA = []
    for i in range(1,tamanho):
        vertorA.append(randint(i, i*100))

    return vertorA
    
    
def fatorial(n):
    fat = n
    for i in range(n-1,1,-1):
        fat = fat * i
    return(fat)


def q8_a(tamanho):
    # a.sequencialmente (sem concorrência)
    t_inicio = float(time.time())

    vetores_A = gera_vetor(tamanho)
    vetores_B = []
    for n in vetores_A:
        vetores_B.append(fatorial(n))

    t_fim = float(time.time())
    return t_fim - t_inicio


def aux_b(vetor_a,inicio,fim,vetor_b_tread):
    try:
        for n in range(inicio,fim):
            vetor_b_tread[n] = fatorial(vetor_a[n])
    except:
        print(n, len(vetor_b_tread))

def q8_b(qntdT,tamanho):
    # b.usando o módulo threading com 4 threads
    import threading

    treads = []
    t_inicio = float(time.time())

    vetor_a = gera_vetor(tamanho)
    vetor_b_tread = vetor_a.copy()

    for i in range(qntdT):
        ini = i * int(tamanho / qntdT)
        fim = (i + 1) * int(tamanho / qntdT)
        t = threading.Thread(target=aux_b,args=(vetor_a,ini,fim,vetor_b_tread))
        t.start()
        treads.append(t)

    for t_ativa in treads:
        t_ativa.join()

    t_fim = float(time.time())
    del treads
    return t_fim - t_inicio



def q8_target(fila_entrada,fila_saida):
    fatiada = fila_entrada.get()
    fila_saida.put([fatorial(n) for n in fatiada])
    
def q8_c(qntdP,tamanho):
    # c.usando o módulo multiprocessing com 4 processos
    import multiprocessing
    t_inicio = float(time.time())

    fila_entrada = multiprocessing.Queue()
    fila_saida = multiprocessing.Queue()

    vetor_a = gera_vetor(tamanho)

    lista_processos = []
    for i in range(qntdP):
        lista_fatiada = vetor_a[i * int(tamanho / qntdP):(i + 1) * int(tamanho / qntdP)]
        fila_entrada.put(lista_fatiada)
        processo = multiprocessing.Process(target=q8_target,args=(fila_entrada,fila_saida))
        processo.start()  # inicia processo 0
        lista_processos.append(processo)

    lista_nova = []
    for i in range(qntdP):
        lista_nova.extend(fila_saida.get())

    t_fim = float(time.time())
    return t_fim - t_inicio


if __name__ == '__main__':
    print(f'Exercício a - tempo: {q8_a(tamanho)}')
    print(f'Exercício b - tempo: {q8_b(4,tamanho)}')
    print(f'Exercício c - tempo: {q8_c(4,tamanho,)}')
