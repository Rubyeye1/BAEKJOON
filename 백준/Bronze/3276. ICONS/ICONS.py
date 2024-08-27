import math
import sys
from collections import deque
import copy
import datetime
from datetime import date, datetime


N = int(sys.stdin.readline())

i = 1

while True:

    if N <= i * i:
        break
    i += 1

resultA = i
resultB = i

while True:
    if resultA * resultB < N:
        resultB += 1
        break
    resultB -= 1

print(resultA, resultB)