s_nums = set([])

for i in range(3, 1000, 3):
    s_nums.add(i)
for i in range(5, 1000, 5):
    s_nums.add(i)

l_nums = list(s_nums)
print(sum(l_nums))