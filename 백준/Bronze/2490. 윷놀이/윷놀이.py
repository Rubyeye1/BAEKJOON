import sys
for i in range(3):
    temp = list(map(int, sys.stdin.readline().split()))
    a = 1
    Dueng = 0
    for i in range(len(temp)):
        if temp[i] == a:
            Dueng = Dueng + 1
    if Dueng == 0:
        print("D")
    elif Dueng == 1:
        print("C")
    elif Dueng == 2:
        print("B")
    elif Dueng == 3:
        print("A")
    else:
        print("E")