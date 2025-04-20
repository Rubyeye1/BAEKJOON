import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

N = int(sys.stdin.readline())
A0 = int(sys.stdin.readline())
result = 0

for _ in range(N):
    temp = int(sys.stdin.readline())

    result += min(abs(temp - A0), 360 - temp + A0, 360 + temp - A0)
    A0 = temp 

print(result)