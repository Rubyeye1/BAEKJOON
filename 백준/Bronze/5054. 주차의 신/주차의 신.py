import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    L = list(map(int, sys.stdin.readline().split()))
    L.sort()
    print((L[-1] - L[0]) * 2)