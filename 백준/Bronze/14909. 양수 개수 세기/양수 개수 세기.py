import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

L = list(map(int, sys.stdin.readline().split()))
result = 0

for i in range(len(L)):
    if L[i] > 0:
        result += 1

print(result)