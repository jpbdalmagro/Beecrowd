inter_wins, gremio_wins, draws, grenais = 0, 0, 0, 0

while True:
    inter_goals, gremio_goals = map(int, input().split())
    grenais += 1
    
    if inter_goals > gremio_goals:
        inter_wins += 1
    elif gremio_goals > inter_goals:
        gremio_wins += 1
    else:
        draws += 1
        
    print('Novo grenal (1-sim 2-nao)')
    if int(input()) == 2:
        break
    
print(f'{grenais} grenais')
print(f'Inter:{inter_wins}')
print(f'Gremio:{gremio_wins}')
print(f'Empates:{draws}')
print(f'{"Inter" if inter_wins > gremio_wins else "Gremio"} venceu mais')
