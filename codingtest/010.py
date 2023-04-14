"""
N(데이터 개수) L(최솟값을 구하는 범위)
mydeque(데이터를 담을 덱 자료구조)
now(주어진 숫자 데이터를 가지는 리스트)
"""
from collections import deque

N, L = map(int, input().split())
mydeque = deque()
now = list(map(int, input().split()))

for i in range(N):
    while mydeque and mydeque[-1][0] > now[i]:
        mydeque.pop()
    mydeque.append((now[i], i))
    if mydeque[0][1] <= i - L:
        mydeque.popleft()
    print(mydeque[0][0], end=" ")