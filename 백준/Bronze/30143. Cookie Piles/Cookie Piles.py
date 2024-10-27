import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

T = int(sys.stdin.readline())

for _ in range(T):
    N, A, D = map(int, sys.stdin.readline().split())
    result = 0
    for i in range(N):
        result += A
        A += D

    print(result)