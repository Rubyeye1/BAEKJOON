import math
import sys
from collections import deque
import copy
import datetime

N, M = map(int, sys.stdin.readline().split())

if len(str(N)*N) <= M:
    print(str(N)*N)
else:
    print((str(N)*N)[:M])