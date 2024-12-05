def converte_nota(nota: int) -> str:
    if nota == 0:
        return 'E'
    elif 1 <= nota <= 35:
        return 'D'
    elif 36 <= nota <= 60:
        return 'C'
    elif 61 <= nota <= 85:
        return 'B'
    elif 86 <= nota <= 100:
        return 'A'
    else:
        return 'Nota invalida'

print(converte_nota(int(input())))
