import math
import sys
from collections import deque
import copy
import datetime


L = []
for i in range(9):
    temp = int(sys.stdin.readline())
    L.append(temp)


checkBreak = 0
resultL = []
for i in range(9):
    if checkBreak == 1:
        break
    for j in range(i+1, 9):

        result = 0

        for k in range(9):
            if k != i and k != j:
                result += L[k]
                resultL.append(L[k])

        if result == 100:
            resultL.sort()
            checkBreak = 1
            for l in range(7):
                print(resultL[l])
            break

        else:
            for q in range(7):
                resultL.pop()