cases = int(input())
nums = [int(input()) for _ in range(cases)]

def is_prime(n: int) -> bool:
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True 

for n in nums:
    if is_prime(n):
        print(f"{n} eh primo")
    else:
        print(f"{n} nao eh primo")
        