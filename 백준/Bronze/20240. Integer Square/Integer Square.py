import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

s = int(sys.stdin.readline())
tempX = -10000
tempY = -10000

for i in range(0, 1000):
    for j in range(0, 1000):
        if (i ** 2 + j ** 2) == s:
            tempX = i
            tempY = j
            break

if tempX == -10000 and tempY == -10000:
    print("Impossible")
else:
    print(0, 0)
    print(tempX, tempY)
    print(tempX - tempY, tempX+tempY)
    print(-tempY, tempX)