import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime


X = int(sys.stdin.readline())
Y = int(sys.stdin.readline())
print("All positions change in year " + str(X))

while True:
    if X + 60 <= Y:
        X += 60
        print("All positions change in year " + str(X))
    else:
        break