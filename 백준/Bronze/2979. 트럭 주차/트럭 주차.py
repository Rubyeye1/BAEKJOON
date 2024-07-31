import math
import sys
from collections import deque
import copy
import datetime

A, B, C = map(int, sys.stdin.readline().split())

L = [0] * 101

ACount = 0
BCount = 0
CCount = 0

for i in range(3):

    Start, End = map(int, sys.stdin.readline().split())

    for j in range(Start, End):
        L[j] += 1

for temp in L:
    if temp == 1:
        ACount += 1
    elif temp == 2:
        BCount += 1
    elif temp == 3:
        CCount += 1

result = (ACount * A) + (BCount * 2 * B) + (CCount * 3 * C)
print(result)