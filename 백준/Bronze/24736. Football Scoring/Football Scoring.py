import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

L1 = list(map(int, sys.stdin.readline().split()))
L2 = list(map(int, sys.stdin.readline().split()))
result = 0

for i in range(len(L1)):
    if i == 0:
        result += L1[i] * 6
    elif i == 1:
        result += L1[i] * 3
    elif i == 2:
        result += L1[i] * 2
    elif i == 3:
        result += L1[i] * 1
    elif i == 4:
        result += L1[i] * 2
print(result)

result = 0
for i in range(len(L2)):
    if i == 0:
        result += L2[i] * 6
    elif i == 1:
        result += L2[i] * 3
    elif i == 2:
        result += L2[i] * 2
    elif i == 3:
        result += L2[i] * 1
    elif i == 4:
        result += L2[i] * 2

print(result)