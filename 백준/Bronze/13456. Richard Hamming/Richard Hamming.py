import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())
    v = list(map(int, sys.stdin.readline().split()))
    u = list(map(int, sys.stdin.readline().split()))
    result = 0

    for i in range(len(v)):
        if v[i] != u[i]:
            result += 1

    print(result)