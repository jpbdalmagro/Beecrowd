time = int(input())
speed = int(input())

distance = time * speed
fuel = distance / 12

print("{:.3f}".format(fuel))
