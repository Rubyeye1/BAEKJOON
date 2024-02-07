import math
import sys

T = int(sys.stdin.readline())
for i in range(T):
    N, M = map(int, sys.stdin.readline().split())
    resultA = 1
    resultB = 1
    tempN = N
    tempM = M
    for i in range(N):
        resultA = resultA * tempN
        tempN = tempN - 1
    for i in range(N):
        resultB = resultB * tempM
        tempM = tempM - 1
    print(int(resultB / resultA))
