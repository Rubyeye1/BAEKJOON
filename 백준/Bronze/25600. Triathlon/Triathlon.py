import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

T = int(sys.stdin.readline())
result = 0

for i in range(T):
    a, d, g = map(int, sys.stdin.readline().split())

    if a == d + g:
        temp = a * (d+g) * 2
    else:
        temp = a * (d+g)

    if temp >= result:
        result = temp

print(result)
