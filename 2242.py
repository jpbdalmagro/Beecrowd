vogais = ['a', 'e', 'i', 'o', 'u']

risada = input()

for letra in risada:
    if letra not in vogais:
        risada = risada.replace(letra, '')

if risada == risada[::-1]:
    print("S")
else:
    print("N")
