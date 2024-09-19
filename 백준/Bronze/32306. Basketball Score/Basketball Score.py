import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

A1, A2, A3 = map(int, sys.stdin.readline().split())
B1, B2, B3 = map(int, sys.stdin.readline().split())
tempA = A1 + A2 * 2 + A3 * 3
tempB = B1 + B2 * 2 + B3 * 3

if tempA > tempB:
    print(1)
elif tempB > tempA:
    print(2)
else:
    print(0)