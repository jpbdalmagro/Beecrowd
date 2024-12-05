data = list(map(int, input().split()))
cormengo = data[0:3]
flaminthians = data[3:6]

pontos_cormengo = sum([3 for x in range(cormengo[0])]) + cormengo[1]
pontos_flaminthians = sum([3 for x in range(flaminthians[0])]) + flaminthians[1]

if pontos_cormengo > pontos_flaminthians:
    print('C')
elif pontos_flaminthians > pontos_cormengo:
    print('F')
else:
    if cormengo[2] > flaminthians[2]:
        print('C')
    elif flaminthians[2] > cormengo[2]:
        print('F')
    else:
        print('=')
