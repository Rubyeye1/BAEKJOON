import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

C = 0

while True:
    C += 1
    L, P, V = map(int, sys.stdin.readline().split())

    if L == 0 and P == 0 and V == 0:
        break

    a = V // P
    b = V % P

    if L < b:
        b = L

    print("Case %d: %d" %(C, (a * L) + b))