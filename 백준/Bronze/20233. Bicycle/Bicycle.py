import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

a = int(sys.stdin.readline())
x = int(sys.stdin.readline())
b = int(sys.stdin.readline())
y = int(sys.stdin.readline())
T = int(sys.stdin.readline())

tempA = x * 21 * max(0, T-30)
tempB = y * 21 * max(0, T-45)
print(tempA + a, tempB + b)