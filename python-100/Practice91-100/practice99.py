import random

numbers = [x for x in range(1, 46)]

def random_number_generate(numbers):
    winning_numbers = random.sample(numbers, 6)
    winning_numbers.sort()
    bonus = random.choice(numbers)
    while bonus in winning_numbers:
        bonus = random.choice(numbers)
    print("<파이썬으로 만든 로또 번호 생성기>")
    print("당첨번호", end=" ")
    for i in winning_numbers[0:6]:
        print(i, end=" ")
    print(f"+ 보너스 {bonus}")

random_number_generate(numbers)