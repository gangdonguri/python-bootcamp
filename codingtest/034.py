"""
N(카드 묶음 개수)
plusPq(양수 우선순위 큐) minusPq(음수 우선순위 큐)
one(1의 개수 카운트) zero(0의 개수 카운트)
"""

from queue import PriorityQueue
N = int(input())
plusPq = PriorityQueue()
minusPq = PriorityQueue()
one = 0
zero = 0
sum = 0

for _ in range(N):
    data = int(input())
    if data > 1:
        data *= -1
        plusPq.put(data)
    elif data < 0:
        minusPq.put(data)
    elif data == 0:
        zero += 1
    else:
        one += 1

while plusPq.qsize() > 1:
    first = plusPq.get() * -1
    second = plusPq.get() * -1
    sum += first * second

if plusPq.qsize() > 0:
    sum += plusPq.get() * -1

while minusPq.qsize() > 1:
    first = minusPq.get()
    second = minusPq.get()
    sum += first * second

if minusPq.qsize() > 0 and zero == 0:
    sum += minusPq.get()

sum += one
print(sum)