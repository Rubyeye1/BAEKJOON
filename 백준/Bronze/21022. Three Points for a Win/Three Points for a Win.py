import math
import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

T = int(sys.stdin.readline())

a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

result = 0

for i in range(T):
    
    if a[i] > b[i]:
        result += 3
    elif a[i] == b[i]:
        result += 1

print(result)