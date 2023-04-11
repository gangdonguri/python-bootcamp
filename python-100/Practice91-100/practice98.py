def bmitest(height, weight):
    bmi = round(weight / (height * 0.01) ** 2, 2)
    print("검사결과")
    print(f"키 : {height}cm 몸무게 : {weight}kg")
    if bmi <= 18.5:
        print(f"저체중 입니다. (BMI지수 {bmi})")
    elif 18.5 < bmi <= 22.9:
        print(f"정상 입니다. (BMI지수 {bmi})")
    elif 23.0 <= bmi <= 24.9:
        print(f"과체중 입니다. (BMI지수 {bmi})")
    else:
        print(f"비만 입니다. (BMI지수 {bmi})")

bmitest(178, 71)