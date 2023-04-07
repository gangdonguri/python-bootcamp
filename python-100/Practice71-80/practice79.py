odd_num = 0
even_num = 0

for i in range(1, 101):
    if i % 2 == 1:
        odd_num += i
    if i % 2 == 0:
        even_num -= i

print(odd_num + even_num)