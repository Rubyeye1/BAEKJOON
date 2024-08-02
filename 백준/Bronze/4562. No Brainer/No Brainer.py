import math
import sys
from collections import deque
import copy
import datetime

T = int(sys.stdin.readline())

for i in range(T):
    a, b = map(int, sys.stdin.readline().split())

    if a >= b:
        print("MMM BRAINS")
    else:
        print("NO BRAINS")
