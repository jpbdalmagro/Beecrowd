def verifica(a, b, c):
    if a < b + c and b < a + c and c < a + b:
        if a == b == c:
            return 'Valido-Equilatero'
        elif a == b or a == c or b == c:
            return 'Valido-Isosceles'
        else:
            return 'Valido-Escaleno'
    else:
        return 'Invalido'


def ret(a, b, c):
    if a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == a**2 + b**2:
        return 'Retangulo: S'
    else:
        return 'Retangulo: N'
    

a, b, c = map(int, input().split())

print(verifica(a, b, c))
print(ret(a, b, c)) if verifica(a, b, c) != 'Invalido' else None
