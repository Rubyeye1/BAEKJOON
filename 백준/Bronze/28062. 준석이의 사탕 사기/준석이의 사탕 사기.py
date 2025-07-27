import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

N = int(sys.stdin.readline())
L = list(map(int, sys.stdin.readline().split()))
odd = []
result = 0

for i in L:
    if i % 2 == 1:
        odd.append(i)
    else:
        result += i

if len(odd) % 2 == 1:
    odd.sort()
    odd.pop(0)
    result += sum(odd)
else:
    result += sum(odd)

print(result)