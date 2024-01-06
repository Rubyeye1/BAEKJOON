while True:
    temp = list(map(int, input().split()))

    temp.sort()

    tempa = int(temp.pop())
    tempb = int(temp.pop())
    tempc = int(temp.pop())





    if tempa == 0 and tempb == 0 and tempc == 0:
        break

    if tempa * tempa == tempc * tempc + tempb * tempb:
        print("right")
    else:
        print("wrong")