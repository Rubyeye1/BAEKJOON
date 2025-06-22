import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

L = []
idx = []
result = 0

for _ in range(8):
    t = int(sys.stdin.readline())
    L.append(t)

for _ in range(5):
    result += max(L)
    idx.append(L.index(max(L)) + 1)

    L[L.index(max(L))] = -100

idx.sort()

print(result)
for i in range(len(idx)):
    print(idx[i], end=" ")