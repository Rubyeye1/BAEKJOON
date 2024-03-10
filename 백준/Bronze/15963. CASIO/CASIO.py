import math
import sys
from collections import deque
import copy

N, M = map(int, sys.stdin.readline().split())

if N == M:
    print(1)
else:
    print(0)