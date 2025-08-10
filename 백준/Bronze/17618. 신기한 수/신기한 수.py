import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

N = int(sys.stdin.readline())
result = 0

for i in range(1, N + 1):
    temp = str(i)
    tempsum = 0

    for j in temp:
        tempsum += int(j)

    if i % tempsum == 0:
        result += 1

print(result)