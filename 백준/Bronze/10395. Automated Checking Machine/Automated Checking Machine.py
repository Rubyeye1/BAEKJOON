import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

L1 = list(map(int, sys.stdin.readline().split()))
L2 = list(map(int, sys.stdin.readline().split()))
L3 = [0, 0, 0, 0, 0]

for i in range(len(L1)):
    if L1[i] == 1:
        L3[i] += 1
    if L2[i] == 1:
        L3[i] += 1

if 2 in L3:
    print("N")
elif 0 in L3:
    print("N")
else:
    print("Y")