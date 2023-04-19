"""
N(노드 개수) M(에지 개수)
A(그래프 데이터 저장 인접 리스트)
visited(방문 기록 저장 리스트)
arrive(도착 확인 변수)
"""

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
N, M = map(int, input().split())
A = [[] for _ in range(N+1)]
visited = [False] * (N+1)
arrive = False

def DFS(now, depth):
    global arrive
    if depth == 5:
        arrive = True
        return
    visited[now] = True
    for i in A[now]:
        if not visited[i]:
            DFS(i, depth + 1)
    visited[now] = False

# 인접 리스트 생성
for _ in range(M):
    s, e = map(int, input().split())
    A[s].append(e)
    A[e].append(s)


for i in range(1, N+1):
    if not visited[i]:
        DFS(i, 1)
        if arrive:
            break

if arrive:
    print(1)
else:
    print(0)