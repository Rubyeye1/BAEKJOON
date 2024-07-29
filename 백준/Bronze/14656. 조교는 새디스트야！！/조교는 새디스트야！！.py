import math
import sys
from collections import deque
import copy
import datetime

N = int(sys.stdin.readline())

L = list(map(int, sys.stdin.readline().split()))

Ltemp = L.copy()
Ltemp.sort()

result = 0

for i in range(N):

    if L[i] != Ltemp[i]:
        result += 1

print(result)