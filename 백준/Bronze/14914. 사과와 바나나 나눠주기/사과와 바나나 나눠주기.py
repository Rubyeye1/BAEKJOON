import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

a, b = map(int, sys.stdin.readline().split())
temp = 0

if a < b:
    temp = a
else:
    temp = b

for i in range(1, temp + 1):
    if a % i == 0 and b % i == 0:
        print(i, int(a / i), int(b / i))