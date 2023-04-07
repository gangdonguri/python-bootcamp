A_CLASS = [70, 60, 90, 80, 100, 50, 80, 90, 45, 100]
total_passers = 0
perfect_score = 0

for score in A_CLASS:
    if score >= 70:
        total_passers += 1
        if score == 100:
            perfect_score += 1

print(f"전체 {len(A_CLASS)}명의 학생 중 총 합격자는 {total_passers}명이고 그 중 만점자는 {perfect_score}명입니다. 아쉽게 불합격한 학생은 {len(A_CLASS)-total_passers}명입니다.")