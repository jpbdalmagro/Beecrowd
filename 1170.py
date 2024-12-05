cases = int(input())

for _ in range(cases):
    days = 0
    food = float(input())
    while food > 1:
        days += 1
        food /= 2
    print(int(days), "dias")
