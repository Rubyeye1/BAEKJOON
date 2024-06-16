import math
import sys
from collections import deque
import copy
import datetime

N, W, H, L = map(int, sys.stdin.readline().split())
result = min((W // L) * (H // L), N)
print(result)