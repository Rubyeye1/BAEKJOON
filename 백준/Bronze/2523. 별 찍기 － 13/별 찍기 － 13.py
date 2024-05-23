import math
import sys
from collections import deque
import copy
import datetime


N = int(sys.stdin.readline())

for i in range(1, N+1):
    for j in range(i):
        print("*", end="")
    print("")
for i in range(N-1, 0, -1):
    for j in range(i):
        print("*", end="")
    print("")
