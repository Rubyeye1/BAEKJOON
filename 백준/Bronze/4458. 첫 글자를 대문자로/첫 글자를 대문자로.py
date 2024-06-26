import math
import sys
from collections import deque
import copy
import datetime

N = int(sys.stdin.readline())

for i in range(N):
    temp = input()
    print(temp[0].upper() + temp[1:])