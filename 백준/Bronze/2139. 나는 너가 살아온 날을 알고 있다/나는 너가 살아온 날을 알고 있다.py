import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

while True:

    i, y, n = map(int, sys.stdin.readline().split())
    if i == 0 and y == 0 and n == 0:
        break

    a = datetime(n, y, i)
    b = datetime(n, 1, 1)

    print((a-b).days + 1)