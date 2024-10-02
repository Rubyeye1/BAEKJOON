import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

T = int(sys.stdin.readline())

for i in range(T):
    a, b = map(int, sys.stdin.readline().split())
    print(a, b)

    if a >= 2:
        print(b * a - ((a-1) * 2))
    else:
        print(b * a)