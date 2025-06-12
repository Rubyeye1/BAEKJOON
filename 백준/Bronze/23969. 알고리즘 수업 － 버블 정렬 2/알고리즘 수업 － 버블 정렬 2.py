import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re


A, K = map(int, sys.stdin.readline().split())
L = list(map(int, sys.stdin.readline().split()))

for i in range(A-1, 0, -1):
    for j in range(i):
        if L[j] > L[j + 1]:
            L[j], L[j + 1] = L[j + 1], L[j]
            K -= 1
        if K == 0:
            print(*L)
            exit()

print(-1)