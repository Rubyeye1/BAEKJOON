import math
import sys
from collections import deque
import copy

N, M = map(int, sys.stdin.readline().split())
print(abs(N-M))