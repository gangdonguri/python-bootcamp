lnums = []

for i in range(100, 79, -1):
    if i % 2 == 0:
        lnums.append(i)

tnums = tuple(lnums)
print(tnums)