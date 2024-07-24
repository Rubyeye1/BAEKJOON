import math
import sys
from collections import deque
import copy
import datetime

T = int(sys.stdin.readline())

for i in range(T):

    a, b = map(str, input().split())
    a = int(a)
    b = list(b)

    for j in range(len(b)):
        if j == (a-1):
            continue
        print(b[j], end="")
    print()