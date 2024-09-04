import math
import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

N = int(sys.stdin.readline())

for _ in range(N):
    A, B, X = map(int, sys.stdin.readline().split())
    print(A * (X - 1) + B)