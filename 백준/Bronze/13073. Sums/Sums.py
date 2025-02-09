import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

t = int(sys.stdin.readline())

for _ in range(t):

    N = int(sys.stdin.readline())

    S1 = N * (N+1) // 2
    S2 = N ** 2
    S3 = (N ** 2) + N

    print(S1, S2, S3)