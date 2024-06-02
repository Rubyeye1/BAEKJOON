import math
import sys
from collections import deque
import copy
import datetime

N = int(sys.stdin.readline())

i = 2
counter = 1
while i * i <= N:

    if N % i == 0:
        counter = N // i
        break

    i += 1

if N == 1:
    print(0)
else:
    print(N-counter)