"""
N(동전 개수) K(목표 금액)
A(동전 데이터 리스트)
"""

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = [0] * N

for i in range(N):
    A[i] = int(input())

count = 0

for i in range(N-1, -1, -1):
    if A[i] <= K:
        count += K // A[i]
        K = K % A[i]

print(count)
