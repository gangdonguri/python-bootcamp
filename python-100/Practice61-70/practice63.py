nums = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

for i in range(1, 11):
    if i % 2 != 0:
        nums.remove(i)

print(nums)