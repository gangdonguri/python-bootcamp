"""
N(노드 개수)
A(그래프 데이터 저장 인접 리스트)
visited 리스트
distance 리스트
"""

from collections import deque

def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] = True

    while queue:
        now_node = queue.popleft()
        for i in A[now_node]:
            if not visited[i[0]]:
                visited[i[0]] = True
                queue.append(i[0])
                distance[i[0]] = distance[now_node] + i[1]

N = int(input())
A = [[] for _ in range(N+1)]

for _ in range(N):
    Data = list(map(int, input().split()))
    index = 0
    S = Data[index]
    index += 1
    while True:
        E = Data[index]
        if E == -1:
            break
        V = Data[index+1]
        A[S].append((E, V))
        index += 2

distance = [0] * (N+1)
visited = [False] * (N+1)

BFS(1)
MAX = 1

for i in range(2, N+1):
    if distance[MAX] < distance[i]:
        MAX = i

distance = [0] * (N+1)
visited = [False] * (N+1)
BFS(MAX)
distance.sort()
print(distance[N])