import math
import sys
from collections import deque
import copy
import datetime

N = int(sys.stdin.readline())
L = list(map(int, sys.stdin.readline().split()))
L.sort()

S = []
for i in range(N):
    if L[i] not in S:
        S.append(L[i])
        print(L[i], end=" ")