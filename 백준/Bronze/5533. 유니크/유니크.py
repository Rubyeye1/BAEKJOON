import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

N = int(sys.stdin.readline())
DL = [[], [], []]

for _ in range(N):
    a, b, c = map(int, sys.stdin.readline().split())
    DL[0].append(a)
    DL[1].append(b)
    DL[2].append(c)
    
for i in range(N):
    temp = 0

    for j in range(3):
        if DL[j].count(DL[j][i]) == 1:
            temp += DL[j][i]

    print(temp)