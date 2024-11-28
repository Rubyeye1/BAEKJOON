import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

A, B = map(int, sys.stdin.readline().split())
resultA = 0
resultB = 0
while True:
    A -= 2
    if A < 0:
        break
    resultA += 1

while True:
    B -= 1
    if B < 0:
        break
    resultB += 1

if resultA > resultB:
    print(resultB)
elif resultB > resultA:
    print(resultA)
else:
    print(resultA)