import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

if N <= 1 or M <= 1:
    print(0)
elif N >= 2 and M >= 2:
    a = N-1
    b = M-1
    result = a * b * 2
    print(result)