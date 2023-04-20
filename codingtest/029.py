"""
N(수 개수 저장)
A(수 데이터 리스트 저장)
M(탐색할 숫자 개수 저장)
target_list(탐색할 수 데이터 리스트 저장)
target(찾아야 하는 수)
start(시작 인덱스)
end(종료 인덱스)
midi(중간 인덱스)
midv(중앙값)
find(일치 여부)
"""

import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
A.sort()
M = int(input())
target_list = list(map(int, input().split()))

for i in range(M):
    find = False
    target = target_list[i]
    start = 0
    end = len(A) - 1

    while start <= end:
        midi = int((start + end) / 2)
        midv = A[midi]
        if target < midv:
            end = midi - 1
        elif target > midv:
            start = midi + 1
        else:
            find = True
            break

    if find:
        print(1)
    else:
        print(0)