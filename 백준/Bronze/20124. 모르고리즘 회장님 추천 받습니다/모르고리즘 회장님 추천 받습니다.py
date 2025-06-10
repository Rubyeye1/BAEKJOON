import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

N = int(sys.stdin.readline())
L = []

for i in range(N):
    name, s = input().split()

    L.append([name, int(s)])

L.sort(key = lambda x: (-x[1], x[0]))

print(L[0][0])