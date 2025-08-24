import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())
D = int(sys.stdin.readline())
E = int(sys.stdin.readline())

if A < 0:
    temp = (-A * C) + D + (B * E)
else:
    temp = (B - A) * E

print(temp)