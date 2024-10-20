import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime


N = int(sys.stdin.readline())

for _ in range(N):

    L = input()
    a = int(L[0])
    b = int(L[2])
    resultA = 0
    resultB = 0

    for i in range(0, 10):
        for j in range(0, 10):

            if i + a > j + b:
                resultA += 1
            elif i + a < j + b:
                resultB += 1
            else:
                if i > b:
                    resultA += 1
                elif i < b:
                    resultB += 1

    print(resultA, resultB)