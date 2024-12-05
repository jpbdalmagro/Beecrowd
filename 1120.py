def remove_erro(erro, n):
    n = str(n)
    if set(n) == {str(erro)}:
        return 0
    return int(n.replace(str(erro), ''))

while True:
    erro, n = map(int, input().split())
    if erro == n == 0:
        break
    n = remove_erro(erro, n)
    
    print(n if n != 0 else 0)
