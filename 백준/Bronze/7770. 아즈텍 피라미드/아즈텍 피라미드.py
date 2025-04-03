import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

n = int(sys.stdin.readline())

h = 0
b = 0

while b <= n:
    b += h ** 2 * 2 + h * 2 + 1
    h += 1

print(h - 1)