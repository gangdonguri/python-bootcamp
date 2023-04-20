"""
N(레슨 개수 저장) M(블루레이 개수 저장)
A(기타 리슨 데이터 저장 리스트)
start(시작 인덱스)
end(종료 인덱스)
middle(중간 인덱스)
sum(레슨 합)
count(현재 사용한 블루레이 개수)
"""

N, M = map(int, input().split())
A = list(map(int, input().split()))
start = 0
end = 0

for i in A:
    if start < i:
        start = i
    end += i

while start <= end:
    middle = int((start + end) / 2)
    sum = 0
    count = 0

    # 중간값 보다 블루레이 크기가 커진 경우 블루레이 추가
    for i in range(N):
        if sum + A[i] > middle:
            count += 1
            sum = 0
        sum += A[i]

    # 위 반복문이 완료되고 남은 레슨이 있는 경우 블루레이 한 개 더 필요
    if sum != 0:
        count += 1
    # 입력 받은 블루레이 개수 보다 더 많이 필요한 경우 블루레이의 크기를 증가
    if count > M:
        start = middle + 1
    else:
        end = middle - 1

print(start)