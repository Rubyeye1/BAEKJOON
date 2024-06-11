import math
import sys
from collections import deque
import copy
import datetime

T = int(sys.stdin.readline())

for i in range(T):
    V, E = map(int, sys.stdin.readline().split())
    print(E - V + 2)