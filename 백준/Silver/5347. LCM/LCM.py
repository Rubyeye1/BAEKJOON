import math
import sys
from collections import deque
import copy

n = int(sys.stdin.readline())

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    result = math.lcm(a, b)
    print(result)