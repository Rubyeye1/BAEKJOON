import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

T = int(sys.stdin.readline())

for _ in range(T):

    N, K = map(int, sys.stdin.readline().split())
    L = list(map(int, sys.stdin.readline().split()))
    result = 0

    for i in range(len(L)):
        result += L[i] // K

    print(result)