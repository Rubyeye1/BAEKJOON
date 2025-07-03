import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

N = int(sys.stdin.readline())
result = 1

if N == 0:
    print(1)
else:
    for i in range(2, N + 1):
        result *= i
        
    print(result)