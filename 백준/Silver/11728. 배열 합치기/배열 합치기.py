import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

N, M = map(int, sys.stdin.readline().split())

A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

C = A + B
C.sort()

for i in C:
    print(i, end=" ")