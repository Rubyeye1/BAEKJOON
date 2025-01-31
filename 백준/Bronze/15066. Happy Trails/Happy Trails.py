import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

n = int(sys.stdin.readline())

result = 0

for _ in range(n):

    a, d = map(int, sys.stdin.readline().split())

    a = math.sin(a * math.pi / 180)

    result += a * d

print("%0.2f"%result)