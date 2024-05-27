import math
import sys
from collections import deque
import copy
import datetime


N = int(sys.stdin.readline())

for i in range(N):
    print(" " * (N-(i+1)) + "* " * i + "*")