import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

N = int(sys.stdin.readline())
result = []

for _ in range(N):
    name = input()

    if len(name) == 3:
        result.append(name)

result.sort()

print(result[0])