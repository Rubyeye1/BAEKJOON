import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

L = input()
L = list(L)

result = 0
result += len(L)

colonCnt = 0
underCnt = 0

for i in range(len(L)):
    if L[i] == ":":
        colonCnt += 1
    if L[i] == "_":
        underCnt += 1

print(result + colonCnt + (underCnt * 5))