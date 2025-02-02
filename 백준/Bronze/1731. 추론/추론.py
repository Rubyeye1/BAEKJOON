import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

N = int(sys.stdin.readline())
L = []

for _ in range(N):
    temp = int(sys.stdin.readline())
    L.append(temp)

if L[1] - L[0] == L[2] - L[1]:
    print(L[-1] + (L[1] - L[0]))
elif L[1] / L[0] == L[2] / L[1]:
    print(L[-1] * int((L[1] / L[0])))