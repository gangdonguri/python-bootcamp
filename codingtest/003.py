import sys
input = sys.stdin.readline
suNo, quizNo = map(int, input().split())
numbers = list(map(int, input().split()))
prefix_sum = [0]
temp = 0

for i in range(suNo):
    temp = prefix_sum[i] + numbers[i]
    prefix_sum.append(temp)

for i in range(quizNo):
    start, end = map(int, input().split())
    print(prefix_sum[end] - prefix_sum[start-1])
