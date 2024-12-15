import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

temp = int(sys.stdin.readline())
N = 1000 - temp
result = 0

while True:
    if N <= 0:
        break
    if N >= 500:
        N -= 500
        result += 1
    elif N >= 100:
        N -= 100
        result += 1
    elif N >= 50:
        N -= 50
        result += 1
    elif N >= 10:
        N -= 10
        result += 1
    elif N >= 5:
        N -= 5
        result += 1
    elif N >= 1:
        N -= 1
        result += 1

print(result)