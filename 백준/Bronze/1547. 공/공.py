import math
import sys
from collections import deque
import copy
import datetime
from datetime import date, datetime


M = int(sys.stdin.readline())

result = 1

for i in range(M):

    a, b = map(int, sys.stdin.readline().split())

    if a == result:
        result = b
    elif b == result:
        result = a

print(result)