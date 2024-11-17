import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

while True:
    temp = int(sys.stdin.readline())
    if temp == 0:
        break
    
    result = 0
    for i in range(1, temp+1, 1):
        result += i
    print(result)