import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

L = int(sys.stdin.readline())
mun = input()
r = 31
M = 1234567891
result = 0

for i in range(len(mun)):
    temp = ord(mun[i]) - 96
    result += temp * (r ** i)
print(result % M)
