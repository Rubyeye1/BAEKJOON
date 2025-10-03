import sys
from collections import deque
import copy
import datetime
from datetime import date, datetime
import re
import math

n, T = map(int, sys.stdin.readline().split())
L = list(map(int, sys.stdin.readline().split()))

for i in range(n):
    if sum(L[:i+1]) > T:
        print(i)
        break
    elif i == n - 1:
        print(n)