"""
N(숫자의 개수) K(K번째 수)
A(숫자 데이터 저장 배열)
"""

import sys
input = sys.stdin.readline
N, K = map(int, input().split())
A = list(map(int, input().split()))

def quickSort(S, E, K):
    global A
    if S < E:
        pivot = partition(S, E)
        if pivot == K:
            return
        elif K < pivot:
            quickSort(S, pivot-1, K)
        else:
            quickSort(pivot+1, E, K)

def swap(i, j):
    global A
    temp = A[i]
    A[i] = A[j]
    A[j] = A[i]

def partition(S, E):
    global A

    # 부분 집합의 개수가 2개만 남은 상황
    if S + 1 == E:
        if A[S] > A[E]:
            swap(S, E)
        return E

    # 중간 값, i, j
    M = (S + E) // 2
    swap(S, M)
    pivot = A[S]
    i = S + 1
    j = E

    while i <= j:
        while pivot < A[j] and j > 0:
            j = j - 1
        while pivot > A[i] and i < len(A) - 1:
            i = i + 1
        # 위 while 문을 통해 얻어진 start와 end 인덱스 값을 swap (start: pivot보다 큰 값을 찾음, end: pivot보다 작은 값을 찾음)
        if i <= j:
            swap(i, j)
            i = i + 1
            j = j - 1

    A[S] = A[j]
    A[j] = pivot
    return j

quickSort(0, N - 1, K - 1)
print(A[K - 1])