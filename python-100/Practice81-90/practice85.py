for i in range(5):
    for j in range(0, i+1):
        print(0, end="")
    for k in range(0, 6-(i+1)):
        print(1, end="")
    print("")