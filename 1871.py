while True:
    x, y = map(int, input().split())

    if x + y == 0:
        break
    
    print(str(x + y).replace('0', ''))
