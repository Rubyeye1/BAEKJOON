import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

L1 = list(map(int, sys.stdin.readline().split()))
L2 = list(map(int, sys.stdin.readline().split()))

resultA = 0
resultB = 0

for i in range(len(L1)):
    if L1[i] > L2[i]:
        resultA += 1
    elif L1[i] < L2[i]:
        resultB += 1

if resultA > resultB:
    print("A")
elif resultB > resultA:
    print("B")
else:
    print("D")
