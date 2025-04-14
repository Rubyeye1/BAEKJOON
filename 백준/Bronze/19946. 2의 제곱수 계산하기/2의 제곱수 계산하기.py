import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

N = int(sys.stdin.readline())
temp = 64

while True:
    if N % 2 == 0:
        N = N // 2
        temp -= 1
    else:
        break

print(temp)