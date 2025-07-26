import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

N = int(sys.stdin.readline())
L = input().split()
s = set()

for i in range(N):
    s.add(L[i][0])

if len(s) == 1:
    print(1)
else:
    print(0)