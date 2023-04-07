num = 13

if num % 10 >= 5:
    num += 10 - num % 10
else:
    num -= num % 10

print(num)