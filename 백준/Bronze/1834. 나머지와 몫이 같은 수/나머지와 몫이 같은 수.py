import math
import sys
from collections import deque
import copy
import datetime

N = int(sys.stdin.readline())

result = 0

for i in range(1, N):
    result += i * N + i

print(result)