import math
a,b,c = 5,6,7

s = (a+b+c)/2
S = math.sqrt(s*(s-a)*(s-b)*(s-c))

print(f"삼각형의 넓이는 {S:.6f}입니다.")