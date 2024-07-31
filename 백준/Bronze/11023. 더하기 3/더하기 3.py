import math
import sys
from collections import deque
import copy
import datetime

L = list(map(int, sys.stdin.readline().split()))

result = 0

for i in range(len(L)):
    result += L[i]

print(result)