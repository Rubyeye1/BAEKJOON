import math
import sys
from collections import deque
import copy

N, M, K = map(int, sys.stdin.readline().split())

tempN = 0
tempM = 0
for i in range(K):
    tempM = tempM + 1
    if tempM == M:
        tempN = tempN + 1
        tempM = 0

print(tempN, tempM)
