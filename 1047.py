entradas = list(map(int, input().split()))
hora_inicial, hora_final = entradas

if hora_final == hora_inicial:
    tempo_horas = 24
else:
    if hora_final < hora_inicial:
        hora_final += 24

    tempo_horas = hora_final - hora_inicial

print(f"O JOGO DUROU {tempo_horas} HORA(S)")