import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

L = []
N = int(sys.stdin.readline())

for _ in range(N):
    D, C = map(int, sys.stdin.readline().split())
    L.append([D, C])

L.sort()

SUK = 100000
result = 0

for i in L:
    temp = i[1]
    
    if temp < SUK:
        SUK = temp
        result += 1

print(result)