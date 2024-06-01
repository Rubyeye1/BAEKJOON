import math
import sys
from collections import deque
import copy
import datetime

N = int(sys.stdin.readline())
L = []

for i in range(N):
    L.append([int(sys.stdin.readline()), i])
    
temp = copy.deepcopy(L)
L.sort()
Max = 0

for i in range(N):
    tempResult = L[i][1] - temp[i][1]
    if Max < tempResult:
        Max = tempResult

print(Max+1)