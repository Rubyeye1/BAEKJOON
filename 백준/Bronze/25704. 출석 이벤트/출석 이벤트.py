import sys
from collections import deque
import copy
import datetime
from datetime import date, datetime
import re
import math

N = int(sys.stdin.readline())
P = int(sys.stdin.readline())
L = [0]

if N >= 5:
    L.append(500)
if N >= 10:
    L.append(P // 10)
if N >= 15:
    L.append(2000)
if N >= 20:
    L.append(P // 4)

result = P - max(L)

if result < 0:
    result = 0

print(result)