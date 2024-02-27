import math
import sys
from collections import deque
import copy

N = int(sys.stdin.readline())
L1 = list(map(int, sys.stdin.readline().split()))
L1 = set(L1)
M = int(sys.stdin.readline())
L2 = list(map(int, sys.stdin.readline().split()))

for i in range(len(L2)):
    if L2[i] in L1:
        print(1, end=" ")
    else:
        print(0, end=" ")