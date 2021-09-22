# Escreva um programa em Python que leia um arquivo texto e apresente na tela o seu conteúdo reverso. Exemplo:
def q4():
    nome_arquivo = 'arquivos/arquivo_q4.txt'
    try:
        with open(nome_arquivo,'r',encoding='utf-8') as arquivo:
            texto = arquivo.readlines()
    except FileNotFoundError as e:
        print(f"O arquivo '{nome_arquivo}' não existe.\nEncerrando aplicação")
        return None

    bn = '\n'
    invertido = [i[::-1].replace(bn, '') for i in texto]
    invertido.reverse()

    print(bn.join(invertido))

q4()