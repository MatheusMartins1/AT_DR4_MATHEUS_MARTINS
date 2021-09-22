import os
import json
import time
from funcoes import formata_tamanho,valida_diretorio

def salva_arquivos(diretorio):

    json_object = json.dumps(diretorio, indent=4)

    with open("arquivos/lista_arquivos.json", "w+",encoding='utf-8') as arquivo_json:
        arquivo_json.write(json_object)

    print(f"Lista de arquivos salvo em '{arquivo_json.name}' ")

def busca_arquivo(arquivo,caminho_diretorio,tamanho):
    try:
        for item in os.listdir(caminho_diretorio):
            if item == arquivo:
             if os.path.isfile(os.path.join(caminho_diretorio, item)):
                 tamanho = os.stat(os.path.join(caminho_diretorio, item)).st_size
             elif os.path.isdir(os.path.join(caminho_diretorio, item)):
                 tamanho += busca_arquivo(item,os.path.join(caminho_diretorio, item), tamanho)
    except FileNotFoundError:
        print("arquivo não encontrado", caminho_diretorio,arquivo)
        pass
    except NotADirectoryError:
        tamanho += os.path.getsize(os.path.join(caminho_diretorio,item))
    except PermissionError:
        print("PermissionError")
        return 0

    return tamanho

def q3(caminho):
    arquivos = {}

    lista_arquivos = os.listdir(caminho)

    for i in lista_arquivos:
       if not os.path.isdir(os.path.join(caminho, i)):
         try:
             idx = lista_arquivos.index(i)
             arquivos[idx] = {}
             nome = os.path.splitext(i)
             arquivos[idx]["nome"] = nome[0]
             arquivos[idx]["tipo"] = nome[1][1:]
             arquivos[idx]["tamanho"] = busca_arquivo(i,caminho,0)
             arquivos[idx]["dt_criacao"] = time.strftime("%d/%m/%Y %H:%M:%S", time.localtime(os.stat(os.path.join(caminho,i)).st_atime))
             arquivos[idx]["dt_modificacao"] = time.strftime("%d/%m/%Y %H:%M:%S", time.localtime(os.stat(os.path.join(caminho,i)).st_mtime))
         except Exception as e:
             print("Erro:",e)

    
    arquivos = [i[1] for i in sorted(arquivos.items(), key=lambda x: x[1]['tamanho'], reverse=True)] #ordenando por tamanho
    
    for a in arquivos:
        index = arquivos.index(a)
        arquivos[index]['tamanho'] = formata_tamanho(a["tamanho"])
    
    return arquivos

def exec_q3():
    caminho_dir = input("Insira diretório: ")
    caminho_dir = valida_diretorio(caminho_dir)
    diretorios = q3(caminho_dir)
    salva_arquivos(diretorios)
    for d in diretorios:
        print(d)