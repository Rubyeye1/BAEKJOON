import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

N, K = map(int, sys.stdin.readline().split())
L = list(map(int, sys.stdin.readline().split(',')))

for _ in range(K):
    temp = [L[i+1] - L[i] for i in range(len(L) - 1)]
    L = temp

print(*L, sep = ',')