import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

N, M = map(int, sys.stdin.readline().split(' '))

L = []

for i in range(N):
    t = int(sys.stdin.readline())
    L.append(t)

temp = 0

for i in range(1, N):
    t = int(sys.stdin.readline())
    temp += t

    if temp >= N - 1:
        print(i)
        break

    temp += L[temp]

    if temp >= N - 1:
        print(i)
        break