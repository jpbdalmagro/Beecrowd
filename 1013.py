inputs = list(map(int, input().split()))
a, b, c = inputs

maiorAB = (a + b + abs(a - b)) / 2
maiorABC = (maiorAB + c + abs(maiorAB - c)) / 2

print(f"{int(maiorABC)} eh o maior")
