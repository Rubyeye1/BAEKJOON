import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

T = int(sys.stdin.readline())

for _ in range(T):
    temp = input()
    N = int(sys.stdin.readline())
    L = []

    for _ in range(N):
        temp2 = int(sys.stdin.readline())
        L.append(temp2)

    result = sum(L)

    if result % N == 0:
        print("YES")
    else:
        print("NO")