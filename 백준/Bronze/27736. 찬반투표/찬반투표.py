import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

N = int(sys.stdin.readline())
L = list(map(int, sys.stdin.readline().split()))
apr = 0
rej = 0
inv = 0

for i in L:
    if i == 1:
        apr += 1
    elif i == -1:
        rej += 1
    else:
        inv += 1

if inv >= N / 2:
    print('INVALID')
elif apr > rej:
    print('APPROVED')
else:
    print('REJECTED')