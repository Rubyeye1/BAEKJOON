import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

L = []
for i in range(9):
    temp = int(sys.stdin.readline())
    L.append(temp)
sum = sum(L)

for i in range(8):
    for j in range(i + 1, 9):
        if sum - (L[i] + L[j]) == 100: 
            temp1 = L[i]
            temp2 = L[j]
            break

for i in range(len(L)):
    if L[i] == temp1 or L[i] == temp2:
        continue
    else:
        print(L[i])