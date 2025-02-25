import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

while True:
    a, b, c, d = map(int, sys.stdin.readline().split())

    if a == 0 and b == 0 and c == 0 and d == 0:
        break

    print(c - b, d - a)