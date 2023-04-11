def square(num):
    for i in range(1, num+1):
        for j in range(1, num+1):
            result = i*j
            if result < 10:
                print(0, end="")
                print(result, end=" ")
            else:
                print(result, end=" ")
        print("")

square(9)