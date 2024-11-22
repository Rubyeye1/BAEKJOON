import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime


T = int(sys.stdin.readline())

for k in range(T):
    x = int(sys.stdin.readline())
    a = input()
    a = list(a)
    b = input()
    b = list(b)

    result = 0

    for i in range(len(a)):
        if a[i] != b[i]:
            result += 1

    print("Case " + str(k+1) + ": " + str(result))