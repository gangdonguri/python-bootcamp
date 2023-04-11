for i in range(9):
    if i <= 4:
        for j in range(i):
            print(0, end="")
        for k in range(9-i*2):
            print(1, end="")
        for o in range(i):
            print(0, end="")
        print("")
    else:
        for j in range(8-i):
            print(0, end="")
        for k in range(i*2-7):
            print(1, end="")
        for o in range(8-i):
            print(0, end="")
        print("")
