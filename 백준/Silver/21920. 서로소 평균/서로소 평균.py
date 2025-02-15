import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

N = int(sys.stdin.readline())
L = list(map(int, sys.stdin.readline().split()))
X = int(sys.stdin.readline())
result = []

for i in range(len(L)):
    if math.gcd(L[i], X) == 1:
        result.append(L[i])

print(sum(result) / len(result))