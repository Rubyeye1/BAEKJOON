import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime


N = int(sys.stdin.readline())
M = []
W = []

for _ in range(N):
    temp = int(sys.stdin.readline())
    M.append(temp)
for _ in range(N):
    temp = int(sys.stdin.readline())
    W.append(temp)

M.sort()
W.sort()
result = 0

for i in range(N):
    a = M[i]
    b = W[i]
    if M[i] > W[i]:
        result += M[i] - W[i]
    elif M[i] < W[i]:
        result += W[i] - M[i]
    else:
        result += M[i] - W[i]

print(result)