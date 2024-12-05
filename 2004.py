for i in range(int(input())):
    alimentos = {}
    
    for c in range(int(input())):
        tipo, peso = input().split()
        peso = int(peso)

        if 1 <= peso <= 100:
            if alimentos.get(tipo):
                if peso > alimentos[tipo]:
                    alimentos[tipo] = peso
            else:
                alimentos[tipo] = peso

    print(sum(alimentos.values()))
