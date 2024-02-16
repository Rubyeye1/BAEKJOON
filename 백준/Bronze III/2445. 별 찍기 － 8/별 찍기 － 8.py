import math
import sys
from collections import deque
import copy

N = int(sys.stdin.readline())

for i in range(1, N+1):
    print("*" * i + " " * (2 * (N-i)) + "*" * i)
for i in range(1, N):
    print("*" * (N-i) + " " * (2 * i) + "*" * (N-i))