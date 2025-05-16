import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

N, D, K = map(int, sys.stdin.readline().split())
L = list(map(int, sys.stdin.readline().split()))
mx = max(L)
temp = 0
result = 0

for _ in range(D):
    temp += mx 

    if temp > K:
        result += 1
        temp = mx

print(result)