N = int(input())

nums = list(map(int, input().split()))

print(f"{len([num for num in nums if num % 2 == 0])} Multiplo(s) de 2")
print(f"{len([num for num in nums if num % 3 == 0])} Multiplo(s) de 3")
print(f"{len([num for num in nums if num % 4 == 0])} Multiplo(s) de 4")
print(f"{len([num for num in nums if num % 5 == 0])} Multiplo(s) de 5")
