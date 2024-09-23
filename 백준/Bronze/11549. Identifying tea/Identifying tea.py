import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

T = int(sys.stdin.readline())
L = list(map(int, sys.stdin.readline().split()))
result = 0

for i in range(len(L)):
    if L[i] == T:
        result += 1

print(result)