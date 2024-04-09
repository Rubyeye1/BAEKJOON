import math
import sys
from collections import deque
import copy
import datetime

N, M = map(int, sys.stdin.readline().split())
N = N - (N * (M / 100))


if N >= 100:
    print("0")
else:
    print("1")