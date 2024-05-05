import math
import sys
from collections import deque
import copy
import datetime

L = list(sys.stdin.readline())

for i in range(0, len(L), 10):
    if i >= len(L):
        break
    for j in range(i, i+10):
        if j >= len(L):
            break
        print(L[j], end="")

    print("")