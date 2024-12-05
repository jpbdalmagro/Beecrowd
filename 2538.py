import sys

def battle(gap: int, atk: int, n_atk: int, gym: list) -> int:
    wins = 0
    gap_min = atk - gap
    gap_max = atk + gap
    
    for i in gym:
        if gap_min <= i <= gap_max:
            wins += 1
    
    return atk if wins <= n_atk else 0

gymnasium = []

# Ler todas as entradas de uma vez
input_data = sys.stdin.read().strip().split()
ip = int(input_data[0])
attempt = int(input_data[1])

index = 2
for _ in range(attempt):
    pc = int(input_data[index])
    na = int(input_data[index + 1])
    index += 2
    
    analogimon = battle(ip, pc, na, gymnasium)
    if analogimon:
        gymnasium.append(analogimon)

print(len(gymnasium))
