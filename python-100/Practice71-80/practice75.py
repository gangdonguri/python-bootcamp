n = 12
fibonacci_numbers = []

for i in range(0, n):
    if i == 0:
        fibonacci_numbers.append(0)
    elif i == 1:
        fibonacci_numbers.append(1)
    else:
        fibonacci_numbers.append(fibonacci_numbers[i-2]+fibonacci_numbers[i-1])

print(fibonacci_numbers)
