import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

T = int(sys.stdin.readline())
L = []

for i in range(T):
    a, b = map(int, sys.stdin.readline().split())
    L.append(a*b)
L.sort()
print(L[-1])