"""
N(카드의 개수) myQueue(카드 저장 자료구조)
"""

from collections import deque
myQueue = deque()

N = int(input())

for i in range(1, N+1):
    myQueue.append(i)

while len(myQueue) > 1:
    myQueue.popleft()
    myQueue.append(myQueue.popleft())

print(myQueue[0])