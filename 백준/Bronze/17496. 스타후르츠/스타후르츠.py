import math
import sys
from collections import deque
import copy
import datetime


N, T, C, P = map(int, sys.stdin.readline().split())
Count = N / T
if Count > int(Count):
    print(int(Count) * C * P)
else:
    print((int(Count)-1) * C * P)