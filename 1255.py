def count_repetitions(frase: list, letras: set) -> dict:
    d = {}
    for letra in letras:
        d[letra] = frase.count(letra)
    return d

cases = int(input())

for i in range(cases):
    text = input().split() 
    text = [l.lower() for x in text for l in x if l.isalpha()]
    letras = set(text)
    d = count_repetitions(text, letras)

    comuns = [k for k, v in d.items() if v == max(d.values())]
    comuns.sort()
    print(''.join(comuns))
