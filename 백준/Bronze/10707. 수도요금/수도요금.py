import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

L = []

for _ in range(5):
    N = int(sys.stdin.readline())
    L.append(N)

X = L[4] * L[0]
Y = L[1] + (L[3] * max(0, L[4] - L[2]))

print(min(X, Y))