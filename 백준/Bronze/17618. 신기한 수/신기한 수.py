import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

N = int(sys.stdin.readline())
result = 0
temp = 0

for i in range(1, N + 1):
    tempA = i
    tempB = 0

    while tempA:
        tempB += tempA % 10
        tempA //= 10

    if i % tempB == 0:
        result += 1
        
print(result)