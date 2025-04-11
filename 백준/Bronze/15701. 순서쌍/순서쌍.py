import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

N = int(sys.stdin.readline())
result = 0
temp = math.sqrt(N)
temp = int(temp)

for i in range(1, temp + 1):

    if N % i == 0:

        if N // i == i:
            result += 1

        else:
            result += 2

print(result)             
        