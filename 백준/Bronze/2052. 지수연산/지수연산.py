import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

N = int(sys.stdin.readline())

result = "%.300f" % (1 / (2 ** N))

for i in range(len(result)-1, 1, -1):
    
    if result[i] != '0':
        temp = i
        break

print(result[:temp+1])