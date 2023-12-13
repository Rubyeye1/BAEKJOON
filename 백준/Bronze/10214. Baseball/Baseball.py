T = int(input())

for i in range(T):
    Yon = 0
    Ko = 0
    for j in range(9):
        tempYon, tempKo = map(int, input().split())
        Yon = Yon + tempYon
        Ko = Ko + tempKo
    if Yon > Ko:
        print("Yonsei")
    elif Ko > Yon:
        print("Korea")
    else:
        print("Draw")