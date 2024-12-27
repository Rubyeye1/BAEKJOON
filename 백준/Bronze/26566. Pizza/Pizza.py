import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

N = int(sys.stdin.readline())

for i in range(N):
    a1, p1 = map(int, sys.stdin.readline().split())
    r1, p2 = map(int, sys.stdin.readline().split())

    temp1 = a1 / p1
    temp2 = (math.pi * (r1 ** 2)) / p2

    if temp1 > temp2:
        print("Slice of pizza")
    else:
        print("Whole pizza")