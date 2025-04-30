import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

N = int(sys.stdin.readline())
L = list(map(int, sys.stdin.readline().split()))
result = [] 

for i in range(N):
    result.append(((i + 1) * L[i]) - sum(result))

for i in range(len(result)):
    print(result[i], end=" ")