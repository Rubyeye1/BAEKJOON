import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime


N = int(sys.stdin.readline())
L = []

for _ in range(N):
    temp = int(sys.stdin.readline())
    L.append(temp)

M = int(sys.stdin.readline())
result = 0

for _ in range(M):
    temp = int(sys.stdin.readline())
    result += L[temp-1]

print(result)