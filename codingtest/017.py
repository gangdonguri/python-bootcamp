"""
A(자릿수별로 구분해 저장한 리스트)
A 리스트 저장
"""

import sys
input = sys.stdin.readline

A = list(input())

print(A)

for i in range(len(A)):
    Max = i
    for j in range(i+1, len(A)):
        if A[j] > A[Max]:
            Max = j
    temp = A[i]
    A[i] = A[Max]
    A[Max] = temp

for i in range(len(A)):
    print(A[i], end="")