import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

temp = []

penalty = 0
result = 0

while True:

    try:
        m, n, r = map(str, sys.stdin.readline().split())

        if r == "right":
            penalty += temp.count(n) * 20
            penalty += int(m)
            result += 1

        temp.append(n)

    except:
        break

print(result, penalty)