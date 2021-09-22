import json
import os

def valida_diretorio(caminho):
    if caminho == "" or not os.path.isdir(caminho):
        print(f"Diretório '{caminho}' não encontrado, realizando busca em {os.getcwd()}")
        caminho = os.getcwd()
    else:
        caminho = caminho
        print(f"Diretório '{caminho}' encontrado, realizando busca...")

    return caminho

def pickle_to_dict(obj):
    obj_json = json.dumps(obj.__dict__,ensure_ascii=False)
    obj_dict = json.loads(obj_json)
    return obj_dict

def formata_tamanho(byte):
    if byte <= 1024:
        return f"{round(byte, 2)}.00 B"
    elif byte <= 1024**2:
        return f"{round(byte / 1024, 2)} KB"
    elif byte <= 1024**3:
        return f"{round(byte / (1024 * 1024), 2)} MB"
    else:
        return f"{round(byte / (1024 * 1024 * 1024), 2)} GB"