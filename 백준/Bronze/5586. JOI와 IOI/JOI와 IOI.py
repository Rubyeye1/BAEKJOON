import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

L = input()

JOIcnt = 0
IOIcnt = 0

for i in range(len(L) - 2):
    temp = ''

    temp += L[i]
    temp += L[i + 1]
    temp += L[i + 2]

    if temp == 'JOI':
        JOIcnt += 1
    elif temp == 'IOI':
        IOIcnt += 1

print(JOIcnt)
print(IOIcnt)