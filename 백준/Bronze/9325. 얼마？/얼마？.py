import math
import sys
from collections import deque
import copy
import datetime

T = int(sys.stdin.readline())
for i in range(T):
    s = int(sys.stdin.readline())
    result = s
    n = int(sys.stdin.readline())
    if n > 0:
        for j in range(n):
            q, p = map(int ,sys.stdin.readline().split())
            result += q * p

    print(result)