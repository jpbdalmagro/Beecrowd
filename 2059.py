inputs = list(map(int, input().split()))
p, j1, j2, r, a = inputs

if r == 1 and a == 1:
    print("Jogador 2 ganha!")
elif r == 1 and a == 0:
    print("Jogador 1 ganha!")
elif r == 0 and a == 1:
    print("Jogador 1 ganha!")
else:
    if (j1 + j2) % 2 == 0:
        if p == 1:
            print("Jogador 1 ganha!")
        else:
            print("Jogador 2 ganha!")
    else:
        if p == 0:
            print("Jogador 1 ganha!")
        else:
            print("Jogador 2 ganha!")
