cases = int(input())
distance = 0

for _ in range(cases):
    info = input().split()
    speed = int(info[0])
    time = int(info[1])
    distance += speed * time
    
print(distance)
