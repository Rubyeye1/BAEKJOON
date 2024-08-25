import math
import sys
from collections import deque
import copy
import datetime
from datetime import date, datetime

result = 0
while True:
    temp = int(sys.stdin.readline())
    if temp == -1:
        break
    result += temp
print(result)