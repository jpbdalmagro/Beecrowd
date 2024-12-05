from math import ceil

def eh_tipico(tipicos: dict, nomes: list, ings: list):
    for ing in ings:
        if ing in nomes:
            ings.remove(ing)
            ings = ings + tipicos[ing]

    i = len([ing for ing in ings if ing in ing_tipicos] )
    
    if i >= ceil(len(ings)) / 2:
        print("porcao tipica")
    else:
        print("porcao comum")

pratos = {}
keys = []

n_ing_tipicos = int(input())
ing_tipicos = list(map(str, input().split()))

cases = int(input())

for i in range(cases):
    nome, qtd_ing = input().split()
    nome = str(nome)
    qtd_ing = int(qtd_ing)
    
    ingredientes = list(map(str, input().split()))
    keys.append(nome)
    pratos[nome] = ingredientes
    
for i in range(cases):
    eh_tipico(pratos, keys, pratos[keys[i]])
