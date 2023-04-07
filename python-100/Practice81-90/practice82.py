work_time = int(input("work time: "))
hourly_wage = 9160

if work_time <= 8:
    print(f"오늘 일당은 {work_time*hourly_wage}원 입니다.")
else:
    print(f"오늘 일당은 {8*hourly_wage+(work_time-8)*(hourly_wage*1.5)}원 입니다.")
