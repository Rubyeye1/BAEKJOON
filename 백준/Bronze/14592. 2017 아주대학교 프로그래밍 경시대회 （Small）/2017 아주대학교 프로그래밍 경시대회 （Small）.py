import sys
from collections import deque
import copy
import datetime
from datetime import date, datetime
import re
import math

N = int(sys.stdin.readline())
L = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

result = sorted(L, key=lambda x:(-x[0], x[1], x[2]))

print(L.index(result[0]) + 1)