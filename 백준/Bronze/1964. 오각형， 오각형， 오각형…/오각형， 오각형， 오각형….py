import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

N = int(sys.stdin.readline())

result = 5
d = 7

for i in range(1, N):
    result += d
    d += 3

print(result % 45678)