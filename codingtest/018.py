"""
N(사람 수)
A(자릿수별로 구분해 저장한 리스트)
S(A 합 배열: 각 사람이 인출을 완료하는 데 필요한 시간을 저장)
"""

import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
S = [0] * N

for i in range(1, N):
    insert_point = i
    insert_value = A[i]
    for j in range(i-1, -1, -1):
        if A[j] < A[i]:
            insert_point = j + 1
            break
        if j == 0:
            insert_point = 0
    for j in range(i, insert_point, -1):
        A[j] = A[j-1]
    A[insert_point] = insert_value

S[0] = A[0]

for i in range(1, N):
    S[i] = S[i-1] + A[i]

sum = 0

for i in S:
    sum += i

print(sum)