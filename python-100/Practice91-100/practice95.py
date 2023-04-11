def rhombus(num):
    for i in range(num):
        for j in range(num-(i+1)):
            print(0, end="")
        for k in range(1+i*2):
            print(1, end="")
        for o in range(num-(i+1)):
            print(0, end="")
        print("")
    for i in range(num-1, -1, -1):
        for j in range(num-(i+1)):
            print(0, end="")
        for k in range(1+i*2):
            print(1, end="")
        for o in range(num-(i+1)):
            print(0, end="")
        print("")

rhombus(12)