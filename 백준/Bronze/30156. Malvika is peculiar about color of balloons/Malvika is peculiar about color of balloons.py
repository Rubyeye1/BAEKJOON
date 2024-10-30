import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

T = int(sys.stdin.readline())

for _ in range(T):
    L = input()
    resultA = 0
    resultB = 0

    for i in range(len(L)):
        if L[i] == "a":
            resultA += 1
        elif L[i] == "b":
            resultB += 1

    if resultA == 0 or resultB == 0:
        print(0)
    elif resultA > resultB:
        print(resultB)
    elif resultB > resultA:
        print(resultA)
    elif resultA == resultB:
        print(resultA)