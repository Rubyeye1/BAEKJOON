import math
import sys
from collections import deque
import copy
import datetime

N = int(sys.stdin.readline())
L = []
for i in range(N):
    temp = int(sys.stdin.readline())
    L.append(temp)

L.sort()
for i in range(N-1, -1, -1):
    print(L[i])