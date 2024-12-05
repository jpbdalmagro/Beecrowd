from math import lcm, sqrt

def encontrar_divisores(n: int) -> list:
    divisores = []
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            divisores.append(i)
            if i != n // i:
                divisores.append(n // i)
    return sorted(divisores)

def validar_tempos(divisores: list, tempo1: int, tempo2: int) -> list:
    tempos = []
    
    for divisor in divisores:
        if lcm(tempo1, tempo2, divisor) == total:
            tempos.append(divisor)
            
    return tempos

while True:
    entrada = list(map(int, input().split()))
    
    if entrada[0] == 0:
        break
    else:
        total, tempo1, tempo2 = entrada
        
        divisores = encontrar_divisores(total)
        tempos = validar_tempos(divisores, tempo1, tempo2)
        
        print(" ".join(map(str, tempos)))
