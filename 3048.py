n = int(input())
ant = 0
mark = 0

seq = [int(input()) for _ in range(n)]

for num in seq:
    if ant == 0:
        mark == 1
        ant = num
    else:
        if num == ant:
            pass
        else:
            mark += 1
        ant = num    

print(mark + 1)
            