import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

T = int(sys.stdin.readline())

for _ in range(T):
    L = list(map(int, sys.stdin.readline().split()))
    L.sort()
    print(L[2] ** 2 + (L[0]+L[1]) ** 2)