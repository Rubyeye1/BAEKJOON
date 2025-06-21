import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

n = int(sys.stdin.readline())
a = 0
b = 1

for i in range(n):
    a, b = b, a + b

print(a)