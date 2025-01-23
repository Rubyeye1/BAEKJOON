import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

t = int(sys.stdin.readline())

for _ in range(t):
    
    n = int(sys.stdin.readline())
    L = list(map(int, sys.stdin.readline().split()))

    temp = 0

    for i in range(len(L)):
        temp += 1
        if temp == L[i]:
            temp += 1

    print(temp)