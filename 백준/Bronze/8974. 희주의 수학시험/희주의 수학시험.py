import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

A, B = map(int, sys.stdin.readline().split())
L = []

for i in range(B):
    if len(L) < B:
        for j in range(i+1):
            L.append(i+1)

print(sum(L[A-1:B]))