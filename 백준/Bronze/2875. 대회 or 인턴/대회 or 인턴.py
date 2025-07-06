import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

N, M, K = map(int, sys.stdin.readline().split())
result = 0

while True:
    N -= 2
    M -= 1

    if N < 0 or M < 0 or (N + M) < K:
        break

    result += 1

print(result)