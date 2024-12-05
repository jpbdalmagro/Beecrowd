N = [int(input()) for x in range(20)]
N_b = []

for n in N:
    N_b.insert(0, n)

for i, n in enumerate(N_b):
    print(f"N[{i}] = {n}")
    