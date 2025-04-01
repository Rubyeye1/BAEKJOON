import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

T = int(sys.stdin.readline())

for _ in range(T):
    
    d, n, s, p = map(int, sys.stdin.readline().split())

    if d + n * p > n * s:
        print("do not parallelize")
    elif d + n * p < n * s:
        print("parallelize")
    else:
        print("does not matter")