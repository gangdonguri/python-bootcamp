# 슬라이싱
# def reverse_print(str):
#     print(str[::-1])

# reverse
def reverse_print(str):
    str_list = list(str)
    str_list.reverse()
    new_str = ''.join(str_list)
    print(new_str)

reverse_print("홍길동은 지금 몹시 화가 났다.")