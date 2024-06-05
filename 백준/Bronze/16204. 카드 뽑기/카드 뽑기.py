import math
import sys
from collections import deque
import copy
import datetime

N, M, K = map(int, sys.stdin.readline().split())

realO, realX = M, N-M
makeO, makeX = K, N-K

result = 0

if realO >= makeO:
    result += makeO
else:
    result += realO

if realX >= makeX:
    result += makeX
else:
    result += realX

print(result)