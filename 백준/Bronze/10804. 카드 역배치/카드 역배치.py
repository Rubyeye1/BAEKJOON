import math
import sys

L = []

for i in range(0, 21):
    L.append(i)

for i in range(10):
    A, B = map(int, sys.stdin.readline().split())
    tempA = A
    tempB = B
    for j in range(A, math.ceil((A+B) / 2)):
        if tempA == tempB or tempA > tempB:
            break
        else:
            L[tempA], L[tempB] = L[tempB], L[tempA]
            tempA = tempA + 1
            tempB = tempB - 1
L.pop(0)

for i in range(len(L)):
    print(L[i], end=" ")