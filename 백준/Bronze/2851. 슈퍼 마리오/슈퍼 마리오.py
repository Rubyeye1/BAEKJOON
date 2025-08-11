import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

L = []
result = 0

for _ in range(10):
    temp = int(sys.stdin.readline())
    L.append(temp)

for i in L:
    result += i

    if result >= 100:
        if result - 100 > 100 - (result - i):
            result -= i
        break

print(result)