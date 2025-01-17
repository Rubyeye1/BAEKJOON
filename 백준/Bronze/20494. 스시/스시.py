import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

N = int(sys.stdin.readline())
result = 0

for _ in range(N):
    temp = input()
    temp = list(temp)
    result += len(temp)

print(result)