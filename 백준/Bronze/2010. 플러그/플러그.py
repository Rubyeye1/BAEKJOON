import math
import sys
from collections import deque
import copy
import datetime

N = int(sys.stdin.readline())
L = []
result = 0
for i in range(N):
    temp = int(sys.stdin.readline())
    L.append(temp)
    result += temp

result -= (N-1)
print(result)