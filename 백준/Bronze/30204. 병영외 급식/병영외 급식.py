import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

N, X = map(int, sys.stdin.readline().split())
L = list(map(int, sys.stdin.readline().split()))

result = 0

for i in range(len(L)):
    result += L[i]

if result % X == 0:
    print(1)
else:
    print(0)