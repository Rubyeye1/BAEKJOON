import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

R, B = map(int, sys.stdin.readline().split())

resultR = 0
resultG = 0

for i in range(1, 10001):
    for j in range(1, 10001):

        if R + B == i * j and (i * 2 + j * 2 - 4) == R:
            resultR = max(i, j)
            resultG = min(i, j)
            break 

print(resultR, resultG)