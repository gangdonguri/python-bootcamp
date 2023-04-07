age = int(input("나이를 입력하세요: "))

if age <= 13:
    print("삐빅, 어린이 입니다.")
elif 14 <= age <= 19:
    print("삐빅, 청소년입니다.")
elif 20 <= age <= 34:
    print("삐빅, 청년입니다.")
elif 35 <= age <= 64:
    print("삐빅, 중장년입니다.")
else:
    print("삐빅, 노인입니다.")