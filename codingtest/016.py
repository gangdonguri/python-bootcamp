"""
N(데이터 개수) A(데이터 리스트, 단 클래스를 데이터로 담는 리스트)
"""

import sys
input = sys.stdin.readline

N = int(input())
A = []

for i in range(N):
    A.append((int(input()), i))

Max = 0
sorted_A = sorted(A)

for i in range(N):
    if Max < sorted_A[i][1] - i:
        Max = sorted_A[i][1] - i

print(Max+1)
