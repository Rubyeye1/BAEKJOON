import math
import sys
from collections import deque
import copy
import datetime
from datetime import date, datetime


while True:
    
    a, b, c, d = map(int, sys.stdin.readline().split())

    if a == 0 and b == 0 and c == 0 and d == 0:
        break
        
    elif a == b and b == c and c == d and d == a:
        print(0)
        
    else:
        
        result = 0

        while True:
            tempA = abs(a - b)
            tempB = abs(b - c)
            tempC = abs(c - d)
            tempD = abs(d - a)

            a = tempA
            b = tempB
            c = tempC
            d = tempD

            result += 1

            if tempA == tempB and tempB == tempC and tempC == tempD and tempD == tempA:
                break

        print(result)
