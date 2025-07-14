import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

N = int(sys.stdin.readline())

for _ in range(N):
    S = int(sys.stdin.readline())

    for i in range(2, 1000001):
        if S % i == 0:
            print("NO")
            break
        elif i == 1000000:
            print("YES")