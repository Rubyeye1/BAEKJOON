import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

T = int(sys.stdin.readline())

for i in range(T):

    N, D = map(int, sys.stdin.readline().split())
    result = 0

    for j in range(N):

        vi, fi, ci = map(int, sys.stdin.readline().split())
        temp = fi / ci
        if temp * vi >= D:
            result += 1

    print(result)