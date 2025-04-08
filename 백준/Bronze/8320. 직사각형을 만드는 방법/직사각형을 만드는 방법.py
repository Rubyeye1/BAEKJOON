import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

n = int(sys.stdin.readline())
result = 0

for i in range(1, n + 1):
    for j in range(i, n + 1):
        if i * j <= n:
            result+=1

print(result)