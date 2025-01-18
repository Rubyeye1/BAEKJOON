import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

N = int(sys.stdin.readline())
N = str(N)
N = list(N)
N = list(map(int, N))

result = 0

for i in range(len(N)):
    temp = N.pop()
    N.insert(0, temp)

    tempRst = ''.join(map(str, N))

    result += int(tempRst)

print(result)