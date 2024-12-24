import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

N, I = map(int, sys.stdin.readline().split())
L = []

for i in range(N):
    a = input()
    L.append(a)

L.sort()

print(L[I-1])