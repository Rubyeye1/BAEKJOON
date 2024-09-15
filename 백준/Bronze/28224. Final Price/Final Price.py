import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime


n = int(sys.stdin.readline())

result = int(sys.stdin.readline())

for i in range(n-1):
    temp = int(sys.stdin.readline())
    result += temp

print(result)