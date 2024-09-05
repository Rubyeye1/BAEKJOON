import math
import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

a, b = map(int, sys.stdin.readline().split())
result = (a / b) * 1000

T = int(sys.stdin.readline())

for _ in range(T):

    a, b = map(int, sys.stdin.readline().split())
    if (a/b) * 1000 < result:
        result = (a/b) * 1000

print("{:.2f}".format(result))