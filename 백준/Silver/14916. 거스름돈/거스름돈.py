import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

n = int(sys.stdin.readline())
result = 0

while True: 
    if n < 0:
        break

    if n % 5 == 0: 
        result += n // 5	
        break
    else:
        result += 1
        n -= 2

if n < 0:
    print(-1)			
else:
    print(result)