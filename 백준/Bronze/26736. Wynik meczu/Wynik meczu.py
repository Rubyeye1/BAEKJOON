import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

W = input()
W = list(W)

resultA = 0
resultB = 0

for i in range(len(W)):
    if W[i] == "A":
        resultA += 1
    else:
        resultB += 1

print(str(resultA) + " : " + str(resultB))