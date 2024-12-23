import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

while True:
    
    a, b = map(int, sys.stdin.readline().split())
    if a == 0 and b == 0:
        break

    resultA = 0
    resultB = 0

    for i in range(a, b+1):

        Yakcnt = 0

        for j in range(1, i+1):
            if i % j == 0:
                Yakcnt += 1

        if Yakcnt >= resultB:
            resultA = i
            resultB = Yakcnt

    print(resultA, resultB)