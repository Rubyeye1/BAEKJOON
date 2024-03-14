import math
import sys
from collections import deque
import copy

a, b = map(int, sys.stdin.readline().split())

resultA = 0
resultB = 0
resultA = math.gcd(a, b)
resultB = math.lcm(a, b)
print(resultA)
print(resultB)