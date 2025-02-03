import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

S1, S2, S3 = map(int, sys.stdin.readline().split())
L = [0] * (S1 * S2 * S3 + 1)

for i in range(1, S1 + 1):
    for j in range(1, S2 + 1):
        for k in range(1, S3 + 1):
            L[i + j + k] += 1

temp = max(L)
result = 0

for i in range(len(L)):
    if L[i] == max(L):
        result = i
        break

print(result)