import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

a, b, c = map(int, sys.stdin.readline().split())

result = 0

for i in range(a, b+1):

    L = list(map(int, str(i)))
    result += L.count(c)

print(result)