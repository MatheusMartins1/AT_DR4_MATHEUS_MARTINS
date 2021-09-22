# 2.	Escreva um programa que obtenha um nome de um arquivo texto do usuário e crie um processo para executar o programa do sistema Windows bloco de notas (notepad) para abrir o arquivo.
import os,subprocess

def q2():
    nome_arquivo = input("Insira o nome do arquivo: ")
    caminho_diretorio = os.getcwd()
    arquivo = os.path.join(caminho_diretorio,"arquivos",nome_arquivo)

    if os.path.isfile(arquivo):
        print(f"Arquivo {arquivo} encontrado. \nabrindo...")

        if nome_arquivo.split('.')[1] == "txt":
            subprocess.run([r'C:\Program Files\Notepad++\notepad++.exe',arquivo])

        else:
            print("O arquivo não é um txt será aberto em modo binário no notepad")
            subprocess.run([r'notepad.exe',arquivo])
    else:
        print(f"Arquivo {arquivo} não encontrado.")

q2()
