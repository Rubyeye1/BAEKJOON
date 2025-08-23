import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

N = int(sys.stdin.readline())

L = [0] * 2000
L[1] = 1
L[2] = 2

for i in range(3, N + 1):
    L[i] = (L[i - 1] + L[i - 2]) % 10007

print(L[N])