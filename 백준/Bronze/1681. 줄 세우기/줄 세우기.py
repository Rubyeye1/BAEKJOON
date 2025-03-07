import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

N, L = map(int, sys.stdin.readline().split())
L = str(L)
temp = 1
result = 0

while True:

    templabel = str(temp)

    if L not in templabel:
        result += 1

    if result == N:
        break

    temp += 1

print(temp)