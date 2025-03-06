import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

N = int(sys.stdin.readline())
L = list(map(int, sys.stdin.readline().split()))
C = int(sys.stdin.readline())
result = 0

for i in range(len(L)):

    temp = L[i]

    if temp == 0:
        continue

    if temp <= C:
        result += C

    else:
        if temp % C > 0:
            result += C * (temp // C + 1)
        else:
            result += C * (temp // C)

print(result)