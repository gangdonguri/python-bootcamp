for i in range(0,5):
    for j in range(4-i, 0, -1):
        print(0, end="")
    for k in range(1, (i+1)*2):
        print(1, end="")
    for o in range(4-i, 0, -1):
        print(0, end="")
    print("")
for i in range(4,-1,-1):
    for j in range(4-i, 0, -1):
        print(0, end="")
    for k in range(1, (i+1)*2):
        print(1, end="")
    for o in range(4-i, 0, -1):
        print(0, end="")
    print("")