import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

T = int(sys.stdin.readline())
for i in range(T):
    a, b = map(int, sys.stdin.readline().split())
    result = 0

    while True:
        a -= b
        result += 1
        if a <= 0:
            break
    print(result)