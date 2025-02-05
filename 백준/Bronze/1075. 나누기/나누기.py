import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

N = int(sys.stdin.readline())
F = int(sys.stdin.readline())

N = N - (N % 100)

while True:
    if N % F == 0:
        break
    else:
        N += 1

print(str(N)[-2], end="")
print(str(N)[-1])