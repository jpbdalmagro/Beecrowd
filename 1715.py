scored = 0

players, games = map(int, input().split())

for i in range(players):
    goals = list(map(int, input().split()))
    if len(list(filter(lambda x: x > 0, goals))) == games:
        scored += 1
        
print(scored)
