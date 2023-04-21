"""
answer(정답 변수)
A 리스트(들어온 데이터를 "-" 기호를 기준으로 split)
"""

answer = 0
A = list(map(str, input().split("-")))

def mySum(i):
    sum = 0
    values = str(i).split("+")
    for value in values:
        sum += int(value)
    return sum

for i in range(len(A)):
    temp = mySum(A[i])
    if i == 0:
        answer += temp
    else:
        answer -= temp

print(answer)