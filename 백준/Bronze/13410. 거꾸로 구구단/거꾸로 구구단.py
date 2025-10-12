import sys
from collections import deque
import copy
import datetime
from datetime import date, datetime
import re
import math

N, K  = map(int, sys.stdin.readline().split())
L = []

for i in range(1, K + 1):
    L.append(int(str(N * i)[::-1]))

print(max(L))