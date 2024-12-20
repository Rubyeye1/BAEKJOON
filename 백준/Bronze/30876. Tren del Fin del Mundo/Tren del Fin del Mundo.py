import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

N = int(sys.stdin.readline())
x = []
y = []

m = 0
cnt = 0
temp = 0
for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    x.append(a)
    y.append(b)
    if m > b:
         m = b
         temp = cnt
    cnt += 1
    
print(x[temp], y[temp])