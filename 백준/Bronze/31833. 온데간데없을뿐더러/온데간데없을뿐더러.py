import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

N = int(sys.stdin.readline())

X = map(str, input().split())
Y = map(str, input().split())

tempX = ''.join(X)
tempY = ''.join(Y)

tempX = int(tempX)
tempY = int(tempY)

if tempX > tempY:
    print(tempY)
elif tempY > tempX:
    print(tempX)
else:
    print(tempX)