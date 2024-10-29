import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

X0, N = map(int, sys.stdin.readline().split())

for _ in range(N):
    if X0 % 2 == 1:
        X0 = (2 * X0) ^ 6
    else:
        X0 = int(X0 / 2) ^ 6

print(X0)