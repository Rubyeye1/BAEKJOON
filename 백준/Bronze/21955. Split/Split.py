import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

n = int(sys.stdin.readline())
L = list(map(int,str(n)))

for i in range(len(L)):
    print(L[i], end="")
    if i == (len(L)/2 - 1):
        print(" ", end="")