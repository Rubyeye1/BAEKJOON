import math
import sys
from collections import deque
import copy
import datetime

L1 = []
L2 = []
N = int(sys.stdin.readline())
for i in range(N):
    temp = input()
    temp = list(temp)
    if temp[0] not in L1:
        L1.append(temp[0])
        L2.append(temp[0])
    else:
        L2.append(temp[0])


result = []
for i in range(len(L1)):
    tempCount = 0
    for j in range(N):
        if L1[i] == L2[j]:
            tempCount = tempCount + 1
    if tempCount >= 5:
        result.append(L1[i])
        
result.sort()

if len(result) == 0:
    print("PREDAJA")
else:
    for i in range(len(result)):
        print(result[i], end="")