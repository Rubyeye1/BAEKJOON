import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

a = []
b = []

for _ in range(3):
    tempA, tempB, tempC = map(str, sys.stdin.readline().split())
    a.append([int(tempA), tempC])
    b.append(tempB)

a.sort(reverse=True)
b.sort()

for i in range(3):
    print(b[i][2], end="")
    print(b[i][3], end="")
print("")
for i in range(3):
    print(a[i][1][0], end="")