import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

N = int(sys.stdin.readline())
L = list(map(int, sys.stdin.readline().split()))
temp = min(L)

for i in range(1, temp + 1):
    cnt = 0

    for j in L:
        if j % i == 0:
            cnt += 1
        else:
            break

    if cnt == N:
        print(i)