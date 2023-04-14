"""
N(질의 요청 개수)
우선순위 큐 선언
- 절댓값 기준으로 정렬되도록 설정
- 단, 절댓값이 같으면 음수 우선 정렬
"""

from queue import PriorityQueue
import sys
input = sys.stdin.readline
print = sys.stdout.write
N = int(input())
myQueue = PriorityQueue()

for i in range(N):
    request = int(input())
    if request == 0:
        if myQueue.empty():
            print('0\n')
        else:
            temp = myQueue.get()
            print(str(temp[1]) + '\n')
    else:
        myQueue.put((abs(request), request))