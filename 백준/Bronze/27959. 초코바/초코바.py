import math
import sys
from collections import deque
import copy
import datetime

N, M = map(int, sys.stdin.readline().split())
if N * 100 >= M:
    print("Yes")
else:
    print("No")