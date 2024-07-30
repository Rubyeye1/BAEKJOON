import math
import sys
from collections import deque
import copy
import datetime

T = int(sys.stdin.readline())

for i in range(T):

    temp = int(sys.stdin.readline())

    result = sum(k * sum(range(k + 2)) for k in range(1, temp + 1))

    print(result)