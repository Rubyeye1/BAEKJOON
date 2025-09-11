import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

N = int(sys.stdin.readline())

for _ in range(N):
    L = list(map(int, sys.stdin.readline().split()))

    print(*L, end=' ')

    if sum(L) == 180:
        print("Seems OK")
    else:
        print("Check")