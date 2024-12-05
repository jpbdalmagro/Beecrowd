cases = int(input())

for _ in range(cases):
    a, b = map(int, input().split())
    
    impares = [x for x in range(min(a, b) + 1, max(a, b)) if x % 2 != 0]
    
    print(sum(impares)) 
    