import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

N = int(sys.stdin.readline())
temp = 0

for i in range(2, N - 1, 2):
    temp += (N - i - 2) // 2

print(temp)