"""
N(노드 개수), M(에지 개수), Start(시작점)
A(그래프 데이터 저장 인접 리스트)
"""

from collections import deque
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
N, M, Start = map(int, input().split())
A = [[] for _ in range(N+1)]

def DFS(v):
    print(v, end=' ')
    visited[v] = True
    for i in A[v]:
        if not visited[i]:
            DFS(i)

def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        now_Node = queue.popleft()
        print(now_Node, end=' ')
        for i in A[now_Node]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

for i in range(M):
    s, e = map(int, input().split())
    A[s].append(e)
    A[e].append(s)

for i in range(1, N+1):
    A[i].sort()

visited = [False] * (N+1)
DFS(Start)
print()
visited = [False] * (N+1)
BFS(Start)
