import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

N = int(sys.stdin.readline())

result = 0

for t in range(1, N + 1):
    for i in str(t):
        if i == '3' or i == '6' or i == '9':
            result += 1

print(result)