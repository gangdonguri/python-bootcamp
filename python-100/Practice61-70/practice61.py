set1 = {1, 2, 3, 4, 5}
list1 = [11, 12, 13, 14, 15]

for i in range(6, 11):
    set1.add(i)

set1.update(list1)
print(set1)