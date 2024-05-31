import math
import sys
from collections import deque
import copy
import datetime


M = int(sys.stdin.readline())
N = int(sys.stdin.readline())
L = []

for i in range(1, 101, 1):

    temp = i * i
    if temp >= M and temp <= N:
        L.append(temp)


PlusResult = 0
MinResult = 0

if len(L) >= 1:
    for i in range(len(L)):
        PlusResult += L[i]
    MinResult = L[0]
    print(PlusResult, MinResult)
else:
    print(-1)