import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

n = int(sys.stdin.readline())
L = list(map(int, sys.stdin.readline().split()))

result = 0

for i in range(n):
    for j in range(n):
        result += abs(L[i] - L[j])

print(result)