n = int(input())
mylist = list(map(int, input().split()))
mymax = max(mylist)
sum = sum(mylist)
print(sum / mymax * 100 / n)
