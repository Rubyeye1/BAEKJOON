import math
import sys
from collections import deque
import copy
import datetime

n = int(sys.stdin.readline())
L = []
for i in range(n):
    temp = int(sys.stdin.readline())
    L.append(temp)

L.sort()

for i in range(n):
    print(L[i])