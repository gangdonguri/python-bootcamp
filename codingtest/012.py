"""
N(수열 개수) A(수열 리스트) ans(정답 리스트)
A 수열 리스트 채우기
myStack(스택 선언)
"""

import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
ans = [0] * N
myStack = []

for i in range(N):
    # 스택이 비어있지 않고 현재 수열이 스택 top 인덱스가 가리키는 수열보다 큰 경우
    while myStack and A[i] > A[myStack[-1]]:
        ans[myStack.pop()] = A[i]
    myStack.append(i)

while myStack:
    ans[myStack.pop()] = -1

for i in range(N):
    print(ans[i], end=" ")

"""
9 5 4 8
"""
