import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
L = list(map(int, sys.stdin.readline().split()))
result = [0] * N

for i in range(M):

    temp = list(map(int, sys.stdin.readline().split()))

    Not = 0

    for j in range(N):
        if temp[j] == L[i]:
           result[j] += 1
        else:
           Not += 1

    result[L[i] - 1] += Not

for i in range(len(result)):
    print(result[i])