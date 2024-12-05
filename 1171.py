nums = []

cases = int(input())

for i in range(cases):
    nums.append(int(input()))
    
qtd_num = len(set(nums))
nums_sorted = sorted(set(nums))

for i in range(qtd_num):
    print(f"{nums_sorted[i]} aparece {nums.count(nums_sorted[i])} vez(es)")
    