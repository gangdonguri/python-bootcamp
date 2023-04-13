"""
n 변수 저장
사용 변수 초기화(count=1, start_index=1, end_index=1, sum=1)
"""

n = int(input())
count = 1
start_index = 1
end_index = 1
sum = 1

while end_index != n:
    if sum < n:
        end_index += 1
        sum += end_index
    elif sum == n:
        count += 1
        end_index += 1
        sum += end_index
    else:
        sum -= start_index
        start_index += 1

print(count)