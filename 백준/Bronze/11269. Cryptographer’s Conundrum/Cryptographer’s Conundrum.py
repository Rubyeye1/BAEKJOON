import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

L = input()
L = list(L)
result = 0

for i in range(len(L)):
    if i % 3 == 0:
        if L[i] != "P":
            result += 1
    elif i % 3 == 1:
        if L[i] != "E":
            result += 1
    elif i % 3 == 2:
        if L[i] != "R":
            result += 1

print(result)