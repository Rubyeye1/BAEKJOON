import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

T = int(sys.stdin.readline())

for _ in range(T):
    
    temp = int(sys.stdin.readline())
    temp = list(str(temp))

    result = []

    for i in range(len(temp)):
        if temp[i] not in result:
            result.append(temp[i])

    print(len(result))