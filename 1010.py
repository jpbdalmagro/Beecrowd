inputs = list(map(float, input().split()))
c1, n1, v1 = inputs
inputs = list(map(float, input().split()))
c2, n2, v2 = inputs

total = n1 * v1 + n2 * v2

print(f"VALOR A PAGAR: R$ {total:.2f}")
