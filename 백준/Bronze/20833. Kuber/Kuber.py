import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

N = int(sys.stdin.readline())
result = 0

for i in range(N):
    result += (i+1) ** 3

print(result)