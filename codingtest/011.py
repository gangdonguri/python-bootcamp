"""
N(수열 개수) A(수열 리스트)
A 수열 리스트 채우기
"""

N = int(input())
A = [0]*N

for i in range(N):
    A[i] = int(input())

stack = []
num = 1
result = True
answer = ""

for i in range(N):
    su = A[i]
    if su >= num:
        while su >= num:
            stack.append(num)
            num += 1
            answer += '+\n'
        stack.pop()
        answer += '-\n'
    else:
        if su < stack[-1]:
            print('NO')
            result = False
            break
        else:
            stack.pop()
            answer += '-\n'

if result:
    print(answer)