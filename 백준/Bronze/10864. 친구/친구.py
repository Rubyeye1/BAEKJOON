import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

N, M = map(int, sys.stdin.readline().split())
L = [0] * N

for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())

    L[A-1] += 1
    L[B-1] += 1

for i in range(len(L)):
    print(L[i])