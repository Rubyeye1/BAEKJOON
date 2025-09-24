import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

while True:
    N = int(sys.stdin.readline())

    if N == 0:
        break

    L = list(map(int, sys.stdin.readline().split()))
    M = 0
    J = 0

    for i in range(len(L)):
        if L[i] == 1:
            J += 1
        else:
            M += 1

    print(f"Mary won {M} times and John won {J} times")