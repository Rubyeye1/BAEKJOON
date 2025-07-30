import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

T = int(sys.stdin.readline())
result = ''
temp = 0

while 9 ** temp <= T:
    temp += 1

for i in range(temp - 1, -1, -1):
    result += str(T // (9 ** i))
    T = T % (9 ** i)

print(result)