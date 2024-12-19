import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())

if A > B:
    print((24 - A) + B)
elif A == B:
    print(24)
else:
    print(B - A)