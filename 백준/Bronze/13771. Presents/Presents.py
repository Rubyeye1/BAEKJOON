import sys
from collections import deque
import copy
import datetime
from datetime import date, datetime
import re
import math


N = int(sys.stdin.readline())
L = []

for _ in range(N):
    temp = input()
    L.append(temp)

L.sort(key=lambda x : float(x))

print(L[1])