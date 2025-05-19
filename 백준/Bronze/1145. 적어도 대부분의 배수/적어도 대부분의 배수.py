import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

L = list(map(int, sys.stdin.readline().split()))
temp = min(L)

while True:
    cnt = 0

    for i in L:
        if temp % i == 0:  
            cnt += 1

    if cnt >= 3:
        print(temp)
        break

    temp += 1   