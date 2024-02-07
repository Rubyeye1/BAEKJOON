import math
import sys

N, K = map(int, sys.stdin.readline().split())
resultA = 1
resultB = 1
tempN = N
tempK = K
for i in range(K):
    resultA = resultA * tempN
    tempN = tempN - 1
for i in range(K):
    resultB = resultB * tempK
    tempK = tempK - 1

print(int(resultA / resultB))