import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

N, M = map(int, sys.stdin.readline().split())


temp = list(map(int, sys.stdin.readline().split()))

for i in range(len(temp)):
    temp[i] = temp[i] % M

result = 1
for i in range(len(temp)):
    result *= temp[i]

result = result % M

print(result)