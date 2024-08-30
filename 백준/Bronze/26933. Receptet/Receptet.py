import math
import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

T = int(sys.stdin.readline())
result = 0

for _ in range(T):

    a, b, c = map(int, sys.stdin.readline().split())

    if a < b:
        result += (b-a) * c

print(result)