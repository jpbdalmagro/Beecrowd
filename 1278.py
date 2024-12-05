linhas = []
i = 0
primeiro_caso = True

while True:
    try:
        linha = input()
    except EOFError:
        break
    inicio = 0
    fim = len(linha) - 1
    while inicio <= fim and linha[inicio] == ' ':
        inicio += 1
    while fim >= inicio and linha[fim] == ' ':
        fim -= 1
    linha = linha[inicio:fim+1]
    if linha:
        linhas.append(linha)
    else:
        break

while i < len(linhas):
    n = int(linhas[i])
    if n == 0:
        break
    
    i += 1
    texto = []
    maior = 0
    for l in range(n):
        linha = linhas[i]
        inicio = 0
        fim = len(linha) - 1
        while inicio <= fim and linha[inicio] == ' ':
            inicio += 1
        while fim >= inicio and linha[fim] == ' ':
            fim -= 1
        linha = linha[inicio:fim+1]
        palavras = linha.split()
        linha_limpa = ' '.join(palavras)
        texto.append(linha_limpa)
        if len(linha_limpa) > maior:
            maior = len(linha_limpa)
        i += 1
    
    if not primeiro_caso:
        print()
    primeiro_caso = False
    
    for linha in texto:
        print(' ' * (maior - len(linha)) + linha)
