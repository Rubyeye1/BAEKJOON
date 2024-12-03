import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

n = int(sys.stdin.readline())
L = list(map(int, sys.stdin.readline().split()))
L.sort()

result = []
for i in range(len(L)):
    if L[i] not in result:
        result.append(L[i])

print(15000 - len(result))