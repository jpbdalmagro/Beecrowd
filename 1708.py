time_a, time_b = map(int, input().split())

i = 1
dif = time_b - time_a
count = 2
while True:
    i += 1
    count += dif
    
    if count >= time_b:
        break

print(i)
