import math
import sys
from collections import deque
import copy
import datetime

T = int(sys.stdin.readline())

for i in range(T):
    temp = list(map(int, sys.stdin.readline().split()))
    temp.sort()
    print(temp[-3])