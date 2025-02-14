import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

N, M = map(int, sys.stdin.readline().split())
Score = list(map(int, sys.stdin.readline().split()))
resultH = []
resultS = []

for _ in range(M):

    L = list(map(str, sys.stdin.readline().split()))
    resultH.append(int(L[0]))

    temp = 0

    for i in range(1, len(L)):
        if L[i] == "O":
            temp += Score[i-1]

    resultS.append(temp)

tempMxScore = max(resultS)
tempL = []

for i in range(len(resultS)):
    if resultS[i] == tempMxScore:
        tempL.append(resultH[i])

print(min(tempL), tempMxScore)