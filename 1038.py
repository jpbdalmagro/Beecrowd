prices = [4.00, 4.50, 5.00, 2.00, 1.50]

code, quantity = map(int, input().split())

total = prices[code - 1] * quantity

print(f'Total: R$ {total:.2f}')
