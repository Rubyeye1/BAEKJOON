import math
import sys
from collections import deque
import copy
import datetime

H,W,N,M = map(int, sys.stdin.readline().split())
i = 1
j = 1
HCount = 0
WCount = 0
while i < H:
    if i + (N+1) > H:
        break
    i += (N+1)
    HCount += 1
while j < W:
    if j + (M+1) > W:
        break
    j += (M+1)
    WCount += 1

print((HCount+1) * (WCount+1))