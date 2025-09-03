import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

N = int(sys.stdin.readline())
temp = 1

while temp * (temp + 1) // 2 < N:
    temp += 1
    
b = N - (temp - 1) * temp // 2
a = temp + 1 - b

print(a, b)