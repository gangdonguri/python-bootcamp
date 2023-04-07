current_weight = 131
week = 0

while current_weight >= 100:
    current_weight -= 2
    week += 1
    print(f"{week}주차 몸무게: {current_weight}")

print(f"{current_weight}kg 달성 성공! 축하드립니다.")