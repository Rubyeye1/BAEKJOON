import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime


N = int(sys.stdin.readline())
result = 0

for _ in range(N):
    q, y = map(float, sys.stdin.readline().split())
    result += q * y

print(result)