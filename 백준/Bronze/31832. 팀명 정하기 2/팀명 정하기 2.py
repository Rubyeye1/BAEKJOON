import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

N = int(sys.stdin.readline())

for _ in range(N):

    temp = input()

    up = 0
    low = 0

    for i in range(len(temp)):
        if temp[i].isupper():
            up += 1
        elif temp[i].islower():
            low += 1

    if up > low:
        continue

    if len(temp) > 10:
        continue

    dig = 0

    for j in range(len(temp)):
        if temp[j].isalpha() or temp[j] == "-":
            dig += 1

    if dig == 0:
        continue

    print(temp)