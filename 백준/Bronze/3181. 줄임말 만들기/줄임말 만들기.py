import sys
from collections import deque
import copy
import datetime
from datetime import date, datetime
import re
import math

L = ['i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili']

temp = input().split()
result = temp[0][0]

for i in range(1, len(temp)):
    if temp[i] in L:
        continue

    result += temp[i][0]

print(result.upper())