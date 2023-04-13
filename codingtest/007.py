"""
N(재료의 개수), M(갑옷이 되는 번호)
A(재료 데이터 저장 리스트)
A 리스트 정렬하기
i(시작 인덱스 = 0)
j(종료 인덱스 = N - 1)
count(정답 값 = 0)
"""
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
A = list(map(int, input().split()))
A.sort()
count = 0
i = 0
j = N - 1

while i < j:
    if A[i] + A[j] < M:
        i += 1
    elif A[i] + A[j] == M:
        count += 1
        i += 1
        j -= 1
    else:
        j -= 1

print(count)
