import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

N = int(sys.stdin.readline())
L = list(map(int, sys.stdin.readline().split()))
result = []
temp = 0

for i in range(N-1):
    if L[i] < L[i+1]:
        temp += L[i+1] - L[i]
    else:
        result.append(temp)
        temp = 0
        
result.append(temp)
print(max(result))