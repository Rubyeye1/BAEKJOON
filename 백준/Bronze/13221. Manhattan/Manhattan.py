import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

x, y = map(int, sys.stdin.readline().split())
N = int(sys.stdin.readline())
m = 10000
resultX = 0
resultY = 0
for i in range(N):
    tempX, tempY = map(int, sys.stdin.readline().split())
    tx = abs(x - tempX)
    ty = abs(y - tempY)
    th = tx + ty

    if m > th:
        m = th
        resultX = tempX
        resultY = tempY

print(resultX, resultY)