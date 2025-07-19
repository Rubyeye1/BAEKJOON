import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

N = int(sys.stdin.readline())
L = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

S = sorted(L, key=lambda x:(-x[0], x[1], x[2]))

print(L.index(S[0]) + 1)