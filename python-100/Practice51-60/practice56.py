import sys

tnums = 1, 2, 3, 4, 5
lnums = [1, 2, 3, 4, 5]

print(f"튜플 tnums과 리스트 lnums의 메모리 사이즈는 각각 {sys.getsizeof(tnums)} bytes, {sys.getsizeof(lnums)} bytes 입니다.")