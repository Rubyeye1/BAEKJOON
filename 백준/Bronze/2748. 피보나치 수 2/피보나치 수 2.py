import math
import sys
from collections import deque
import copy
import datetime

n = int(sys.stdin.readline())
L = [0] * 100

L[0] = 0
L[1] = 1

for i in range(n):
    L[i+2] = L[i]+L[i+1]

print(L[n])