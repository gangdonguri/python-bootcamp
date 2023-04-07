num1,num2,num3 = 15,23,9

if (num1 > num2) and (num1 > num3):
    print(f"가장 큰 수를 가지고 있는 변수는 값이 {num1}인 num1입니다.")
elif (num2 > num1) and (num2 > num3):
    print(f"가장 큰 수를 가지고 있는 변수는 값이 {num2}인 num2입니다.")
elif (num3 > num1) and (num3 > num2):
    print(f"가장 큰 수를 가지고 있는 변수는 값이 {num3}인 num3입니다.")
else:
    print("모두 같습니다.")
