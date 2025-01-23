import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

while True:

    n = int(sys.stdin.readline())
    if n == 0:
        break

    L = []
    tempL = []

    for i in range(n):
        temp = input()
        L.append([temp, i])
        temp = temp.lower()
        tempL.append([temp, i])

    tempL.sort()
    rstidx = tempL[0][1]

    for i in range(n):
        if L[i][1] == rstidx:
            print(L[i][0])
            break