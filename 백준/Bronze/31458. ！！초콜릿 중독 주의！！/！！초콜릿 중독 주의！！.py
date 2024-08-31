import math
import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

T = int(sys.stdin.readline())

for i in range(T):

    L = list(input())

    a = 0
    b = 0
    idx = 0

    for j in range(len(L)):
        if L[j] == "0" or L[j] == "1":
            idx = j
            break
        if L[j] == "!":
            a += 1

    for k in range(idx+1, len(L)):
        if L[k] == "!":
            b += 1

    temp = int(L[idx])

    if b != 0:
        temp = 1

    if a != 0:
        if a % 2 == 1:
            if temp == 0:
                temp = 1
            else:
                temp = 0

    print(temp)