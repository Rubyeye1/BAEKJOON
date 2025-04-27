import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

N, M, L = map(int, sys.stdin.readline().split())
p = [0] * N
p[0] = 1
i = 0
throw = 0

while True:
    if p[i] == M:
        print(throw)
        break

    if p[i] % 2 == 1:
        i = (i + L) % N
        p[i] += 1
        throw += 1     
    else:
        i = abs((i - L) % N)
        p[i] += 1
        throw += 1