import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

n = int(sys.stdin.readline())
L = list(map(int, str(n)))
result = 0

for i in range(len(L)):
    result += L[i] ** 5

print(result)