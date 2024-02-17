import math
import sys
from collections import deque
import copy

N = int(sys.stdin.readline())

for i in range(N):
    print(" " * i + "*" * ((2 * N - 1) - (2 * i)))
for i in range(N-1, 0, -1):
    print(" " * (i-1) + "*" * ((2 * N + 1) - (2 * i)))