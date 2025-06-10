import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

M = int(sys.stdin.readline())
S = set()

for _ in range(M):
    temp = sys.stdin.readline().split()

    if len(temp) == 1:
        if temp[0] == 'all':
            S = set(range(1, 21))
        else:
            S = set()
    else:
        mr = temp[0]
        x = int(temp[1])

        if mr == "add":
            S.add(x)

        if mr == "remove":
            S.discard(x)

        if mr == "check":
            print(1 if x in S else 0)

        if mr == "toggle":
            if x in S:
                S.discard(x)
            else:
                S.add(x)