import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

n = int(sys.stdin.readline())
L = list(map(int, sys.stdin.readline().split()))
L.sort()

result = 0

for i in range(len(L)-1):
    result += L[i]
    
print(result)