casos = int(input())

for i in range(casos):
    codigo = input().strip()
    decodificador = int(input().strip())
    
    decodificado = ""
    for char in codigo:
        nova_posicao = ord(char) - decodificador
        if nova_posicao < ord('A'):
            nova_posicao += 26
        decodificado += chr(nova_posicao)
    
    print(decodificado)
    