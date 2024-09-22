import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

a, b = map(int, sys.stdin.readline().split())

if a > b:
    print(a)
elif b > a:
    print(b)
else:
    print(a)