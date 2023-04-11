num = 24
d = 2
result = ""

while d <= num:
    if num % d == 0:
        if num == d:
            result += str(d)
        else:
            result += str(d) + " "
        num /= d
    else:
        d += 1

new_result = result.replace(" ", " * ")
print(f"num = {new_result}")