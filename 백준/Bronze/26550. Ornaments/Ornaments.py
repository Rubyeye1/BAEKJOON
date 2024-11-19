import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime


n = int(sys.stdin.readline())

for _ in range(n):
    m = int(sys.stdin.readline())
    result = 0
    temp = 0
    
    for i in range(1, m+1, 1):
        temp += i
        result += temp
        
    print(result)