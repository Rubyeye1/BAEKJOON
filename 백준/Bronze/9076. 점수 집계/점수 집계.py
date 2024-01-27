import sys

N = int(sys.stdin.readline())
for i in range(N):
    L = list(map(int, sys.stdin.readline().split()))
    L.sort()
    result = 0
    if L[3] - L[1] >= 4:
        print("KIN")
    else:
        for i in range(1, 4):
            result = result + L[i]
        print(result)