# 5.	Escreva um programa em Python que leia dois arquivos_q5, a.txt e b.txt, como a seguir: Seu programa deve somar elemento por elemento de cada arquivo e imprimir o resultado na tela. Isto é, o primeiro elemento de a.txt deve ser somado ao primeiro elemento de b.txt, segundo elemento de a.txt deve ser somado ao segundo elemento de b.txt, e assim sucessivamente. Caso um arquivo tenha mais elementos que o outro, os elementos que sobrarem do maior devem ser somados a zero.
arquivos_q5 = {}

def q5():
    tamanho = 0
    soma = 0
    for arq in ("a","b"):
        arquivo_dir = f'arquivos/{arq}.txt'
        try:
            with open(arquivo_dir, 'r', encoding='utf-8') as arq_byte:
                texto = arq_byte.read().split(" ")

            tamanho_texto = len(texto)
            arquivos_q5[arq] = {'tamanho': tamanho_texto,'elementos': texto}

            tamanho = tamanho if tamanho_texto < tamanho else tamanho_texto
        except FileNotFoundError as e:
            print(f"O arquivo '{arquivo_dir}' não existe.\nEncerrando aplicação")
            return None



    total = []
    for el in range(tamanho):
        for letra in arquivos_q5:
                try:
                    valor = int(arquivos_q5[letra]['elementos'][el])
                    soma += valor
                    print(f"arquivo:{letra} | contador:{el} | valor: {valor}")
                except IndexError:
                    print(f"arquivo:{letra} | contador:{el} | valor: '' | Somando a zero: {soma}")

        total.append(soma)
        soma = 0

    return total

resultado = q5()
if resultado != None:
    print(f"\nTotal somado: {resultado} | soma dos valores somados: {sum(resultado)}")
    print(f"Arquivo a: {arquivos_q5['a']['elementos']}")
    print(f"Arquivo b: {arquivos_q5['b']['elementos']}")