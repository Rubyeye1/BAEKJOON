import math
import sys
from collections import deque
import copy
import datetime

total = int(sys.stdin.readline())

for i in range(9):
    temp = int(sys.stdin.readline())
    total -= temp

print(total)