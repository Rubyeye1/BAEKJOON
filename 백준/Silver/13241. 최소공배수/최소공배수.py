import math
import sys
from collections import deque
import copy
import datetime

a, b =map(int, sys.stdin.readline().split())
result = math.lcm(a,b)
print(result)