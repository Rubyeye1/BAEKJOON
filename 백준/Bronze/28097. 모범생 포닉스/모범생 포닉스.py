import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

N = int(sys.stdin.readline())
L = list(map(int, sys.stdin.readline().split()))
temp = 0

for i in range(len(L)):
    temp += L[i]

temp += 8 * (N - 1)

print(temp // 24, temp % 24)