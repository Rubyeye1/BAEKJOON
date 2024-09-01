import math
import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

L = list(map(int, sys.stdin.readline().split()))

L.sort()

a = L[1] - L[0]
b = L[2] - L[1]

if a < b:
    print(L[1] + a)
elif a > b:
    print(L[0] + b)
elif a == b:
    print(L[2] + a)