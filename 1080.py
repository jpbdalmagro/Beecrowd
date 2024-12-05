nums = [int(input()) for _ in range(100)]
biggier = max(nums)
position = nums.index(biggier) + 1

print(biggier)
print(position)
