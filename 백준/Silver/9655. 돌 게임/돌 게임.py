import math
import sys
from collections import deque
import copy
import datetime

N = int(sys.stdin.readline())
count = 0
while True:
    if N <= 0:
        break
    else:
        if N % 3 == 2:
            N = N - 1
            count = count + 1
        elif N % 3 == 1:
            N = N - 3
            count = count + 1
        else:
            N = N - 3
            count = count + 1

if count % 2 == 1:
    print("SK")
else:
    print("CY")