import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

while True:
    A, B = map(int, sys.stdin.readline().split())

    if A == 0 and B == 0:
        break
    else:
        print(2 * A - B)