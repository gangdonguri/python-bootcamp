"""
N(데이터 개수)
Result(좋은 수 개수 저장 변수)
A(수 데이터 저장 리스트)
A 리스트 정렬
"""
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
A.sort()
Result = 0

for K in range(N):
    i = 0
    j = N - 1
    while i < j:
        if A[i] + A[j] == A[K]:
            if i != K and j != K:
                Result += 1
                break
            elif i == K:
                i += 1
            elif j == K:
                j -= 1
        elif A[i] + A[j] < A[K]:
            i += 1
        else:
            j -= 1

print(Result)
