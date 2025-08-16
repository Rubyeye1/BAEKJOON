import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

resultA = 0
resultB = 0
N = int(sys.stdin.readline())

for _ in range(N):
    A, B = map(int, sys.stdin.readline().split())

    if A > B:
        resultA += 1
    elif A < B:
        resultB += 1

print(resultA, resultB)