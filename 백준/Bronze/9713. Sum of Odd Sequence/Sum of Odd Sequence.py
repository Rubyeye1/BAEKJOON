import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

T = int(sys.stdin.readline())

for _ in range(T):

    temp = int(sys.stdin.readline())
    result = 0

    for i in range(1, temp+1, 2):
        if i % 2 == 1:
            result += i

    print(result)
