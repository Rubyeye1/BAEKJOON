import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

N = int(sys.stdin.readline())

for i in range(1, N+1):
    if 1 + i + (i ** 2) == N:
        print(i)
        break