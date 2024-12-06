import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

N, M = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
result = []

for j in range(len(a)):
    for i in range(1, N+1):
        if i % a[j] == 0:
            if i not in result:
                result.append(i)

fnl = 0
for i in range(len(result)):
    fnl += result[i]

print(fnl)