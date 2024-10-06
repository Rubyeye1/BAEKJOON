import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

N = int(sys.stdin.readline())

arr = [list(map(int, input().split())) for _ in range(N)]

min_val = min(map(min, arr))

if min_val == arr[0][0]:
    print(0)
elif min_val == arr[0][N-1]:
    print(1)
elif min_val == arr[N-1][N-1]:
    print(2)
elif min_val == arr[N-1][0]:
    print(3)