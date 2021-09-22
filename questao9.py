# Dado um vetor A de tamanho N com apenas números inteiros positivos, calcule o fatorial de cada um deles e armazene o resultado em um vetor B
# Para calcular o fatorial, utilize a seguinte função:
import time
from random import randint,random
import json
from questao8 import q8_a,q8_b,q8_c,vetor_b_tread

tamanho = 10

tamanhos = {
    1:{"tamanho":1000000},
    2:{"tamanho":5000000},
    3:{"tamanho":10000000},
}

# tamanhos = {
#     1:{"tamanho":10},
#     2:{"tamanho":50},
#     3:{"tamanho":100},
# }

if __name__ == '__main__':
    
    for i in tamanhos:
        global vetor_b_tread
        vetor_b_tread = []
        tamanhos[i]['Sequencial'] = q8_a(tamanhos[i]["tamanho"])
        tamanhos[i]['Threading'] = q8_b(4,tamanhos[i]["tamanho"])
        tamanhos[i]['Multiprocessing'] = q8_c(4,tamanhos[i]["tamanho"])
    
    print(json.dumps(tamanhos, indent=4, sort_keys=True), '\n')
    # print(f'Exercício a - tempo: {q8_a(tamanho)}')
    # print(f'Exercício b - tempo: {q8_b(tamanho)}')
    # print(f'Exercício c - tempo: {q8_c(4,tamanho,)}')