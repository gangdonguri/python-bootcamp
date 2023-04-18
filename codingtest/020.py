"""
병합 정렬(s, e):
    s(시작점), e(종료점), m(중간점)
    병합 정렬(s, m)
    병합 정렬(m + 1, e)
    for s ~ e:
        tmp 리스트 저장

    index1 = 앞쪽 그룹 시작점
    index2 = 뒤쪽 그룹 시작점
    while index1 <= 중간점 and index2 <= 종료점:
"""

import sys
input = sys.stdin.readline
print = sys.stdout.write

def merge_sort(s, e):
    if e -s < 1:
        return
    m = int(s + (e - s) / 2)
    merge_sort(s, m)
    merge_sort(m+1, e)
    for i in range(s, e+1):
        tmp[i] = A[i]
    k = s
    index1 = s
    index2 = m + 1

    while index1 <= m and index2 <= e:
        if tmp[index1] > tmp[index2]:
            A[k] = tmp[index2]
            k += 1
            index2 += 1
        else:
            A[k] = tmp[index1]
            k += 1
            index1 += 1

    while index1 <= m:
        A[k] = tmp[index1]
        k += 1
        index1 += 1

    while index2 <= e:
        A[k] = tmp[index2]
        k += 1
        index2 += 1

N = int(input())
A = [0] * (N+1)
tmp = [0] * (N+1)

for i in range(1, N+1):
    A[i] = int(input())

merge_sort(1, N)

for i in range(1, N+1):
    print(str(A[i]) + '\n')

"""
1 2 3 4 5
5 4 3 2 1
"""