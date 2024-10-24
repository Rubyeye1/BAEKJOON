import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime


n = int(sys.stdin.readline())
L = []

for _ in range(n):
    result = 0
    t, l = map(int, sys.stdin.readline().split())
    result = t + l
    L.append(result)
L.sort()
print(L[0])