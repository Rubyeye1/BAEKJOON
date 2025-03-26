import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

n = int(sys.stdin.readline())
L = list(map(int, sys.stdin.readline().split()))
D = list(map(int, sys.stdin.readline().split()))

for i in range(len(D)):
    if D[i] in L:
        L.remove(D[i])

for i in range(len(L)):
    print(L[i])