import math

p1 = list(map(float, input().split()))
p2 = list(map(float, input().split()))

x1, y1 = p1
x2, y2 = p2

distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print(f"{distance:.4f}")
