import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

N = int(sys.stdin.readline())
L = list(map(float, sys.stdin.readline().split()))
result = 0

for i in L:
    result += i ** 3
    
print(result ** (1 / 3))