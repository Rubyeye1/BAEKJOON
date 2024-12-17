import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

N = int(sys.stdin.readline())

L = list(map(int, sys.stdin.readline().split()))
result = []
no = 0
for i in range(len(L)):
    if L[i] not in result:
        result.append(L[i])
    else:
        no += 1

print(no)