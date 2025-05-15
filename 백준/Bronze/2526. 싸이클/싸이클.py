import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

N, P = map(int, sys.stdin.readline().split())
temp = N 
L = []

while True:
    temp = (temp * N) % P

    if temp in L:
        break

    L.append(temp)

print(len(L) - L.index(temp)) 