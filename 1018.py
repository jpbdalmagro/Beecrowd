money = int(input())

print(money)
print(f'{money // 100} nota(s) de R$ 100,00')
money %= 100
print(f'{money // 50} nota(s) de R$ 50,00')
money %= 50
print(f'{money // 20} nota(s) de R$ 20,00')
money %= 20
print(f'{money // 10} nota(s) de R$ 10,00')
money %= 10
print(f'{money // 5} nota(s) de R$ 5,00')
money %= 5
print(f'{money // 2} nota(s) de R$ 2,00')
money %= 2
print(f'{money // 1} nota(s) de R$ 1,00')
money %= 1
