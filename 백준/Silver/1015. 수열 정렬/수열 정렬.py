import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

N = int(sys.stdin.readline())
L = list(map(int, sys.stdin.readline().split()))
temp = L.copy()
L.sort()
result = [0] * N

for i in range(N):
    for j in range(N):
        if L[j] == temp[i]:
            result[i] = j
            L[j] = -10
            break

for i in range(len(result)):
    print(result[i], end=" ")