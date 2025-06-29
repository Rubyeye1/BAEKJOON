import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

N = int(sys.stdin.readline())
L = list(map(int, sys.stdin.readline().split()))
result = 0

for i in range(N):
    if L[i] == result % 3:
        result += 1

print(result)