import math
import sys
from collections import deque
import copy
import datetime

N = int(sys.stdin.readline())

x = []
y = []

for i in range(N):
    a, b = map(int,sys.stdin.readline().split())
    x.append(a)
    y.append(b)

MaxX = max(x)
MaxY = max(y)
MinX = min(x)
MinY = min(y)

if N == 1:
    print(0)
else:
    print((MaxX-MinX) * (MaxY-MinY))