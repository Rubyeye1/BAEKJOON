import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())
    result = 0

    for i in range(1, n):
        if i ** 2 <= n:
            result += 1
        elif i ** 2 > n:
            break
    
    print(result)