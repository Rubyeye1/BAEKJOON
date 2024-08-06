import math
import sys
from collections import deque
import copy
import datetime
from datetime import date, datetime

N = int(sys.stdin.readline())

result = 0

for i in range(1, 501):
    for j in range(i, 501):
        if (j * j) - (i * i) == N:
            result += 1

print(result)