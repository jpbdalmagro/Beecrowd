x = int(input())
y = int(input())

soma = sum([i for i in range(min(x, y) + 1, max(x, y)) if i % 2 != 0])

print(soma)