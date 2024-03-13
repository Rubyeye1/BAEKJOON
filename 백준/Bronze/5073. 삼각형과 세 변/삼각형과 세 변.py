import math
import sys
from collections import deque
import copy

while True:
    A, B, C = map(int, sys.stdin.readline().split())

    if A == 0 and B == 0 and C == 0:
        break

    L = []
    L.append(A)
    L.append(B)
    L.append(C)
    L.sort()

    if L[0] + L[1] <= L[2]:
        print('Invalid')
    elif A == B and B == C and C == A:
        print('Equilateral')
    elif A == B or B == C or C == A:
        print('Isosceles')
    else:
        print("Scalene")