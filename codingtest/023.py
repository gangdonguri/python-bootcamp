"""
n(노드 개수) m(에지 개수)
A(그래프 데이터 저장 인접 리스트) 초기화
visited(방문 기록 리스트) 초기화
"""

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
n, m = map(int, input().split())
A = [[] for _ in range(n+1)]
visited = [False] * (n+1)

def DFS(v):
    visited[v] = True
    for i in A[v]:
        if not visited[i]:
            DFS(i)

# 인접 리스트 생성
for _ in range(m):
    s, e = map(int, input().split())
    A[s].append(e)
    A[e].append(s)

count = 0

# 방문하지 않은 노드 탐색
for i in range(1, n+1):
    if not visited[i]:
        count += 1
        DFS(i)

print(count)

