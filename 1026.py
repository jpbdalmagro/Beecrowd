import sys

sum = []

input_data = sys.stdin.read().strip()

for line in input_data.split('\n'):
    x, y = map(int, line.split())
    
    x = str(bin(x)[2:])
    y = str(bin(y)[2:])

    x = x.zfill(32)
    y = y.zfill(32)

    temp_sum = []
    for i in range(32):
        if x[i] != y[i]:
            temp_sum.append(1)
        else:
            temp_sum.append(0)
    
    temp_sum = ''.join(map(str, temp_sum))
    sum.append(int(temp_sum, 2))

for result in sum:
    print(result)
