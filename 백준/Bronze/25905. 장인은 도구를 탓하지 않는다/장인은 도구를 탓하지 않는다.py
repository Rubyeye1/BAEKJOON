import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

L = []

for _ in range(10):
    temp = float(sys.stdin.readline())
    L.append(temp)

result = 1

for i in range(len(L)):
    result *= L[i]
    
result /= min(L)
result /= 0.00036288

print(round(result,6))