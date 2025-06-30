import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

N = int(sys.stdin.readline())
L = list(map(int, sys.stdin.readline().split()))

mx = -1
cnt = 0
result = []

for i in L:
    if i > mx:
        mx = i
        cnt = 0
    else:
        cnt += 1

    result.append(cnt)

print(max(result))