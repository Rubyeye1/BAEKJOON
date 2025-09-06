import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

N, M = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

if N < M:
    a += [0] * (M - N)

result = 0

for i in range(M):
    result = max(result, b[i] - a[i])

print(result)