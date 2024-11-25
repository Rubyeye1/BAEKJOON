import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime


N = int(sys.stdin.readline())
L = []
for _ in range(N):
    temp = input()
    L.append(temp)

I = L.copy()
D = L.copy()
I.sort()
D.sort(reverse=True)

if L == I:
    print("INCREASING")
elif L == D:
    print("DECREASING")
else:
    print("NEITHER")