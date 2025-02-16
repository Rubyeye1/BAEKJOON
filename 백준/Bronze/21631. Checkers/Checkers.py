import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

a, b = map(int, sys.stdin.readline().split())

if a < b and b != 0:
    print(a + 1)
elif a >= b:
    print(b)