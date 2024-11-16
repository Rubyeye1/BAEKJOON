import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

n, m = map(int, sys.stdin.readline().split())
result = 0

for _ in range(n):
    L = input()

    if "+" in L:
        result += 1

print(result)