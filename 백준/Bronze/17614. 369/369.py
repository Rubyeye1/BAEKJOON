import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

N = int(sys.stdin.readline())
result = 0

for i in range(1, N + 1):
    result += str(i).count('3') + str(i).count('6') + str(i).count('9')\
    
print(result)