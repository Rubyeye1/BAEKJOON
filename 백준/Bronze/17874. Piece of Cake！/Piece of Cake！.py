import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

n, h, v = map(int, sys.stdin.readline().split())

tempH = 0
tempV = 0

if h < n / 2:
    tempH = n - h
else:
    tempH = h

if v < n / 2:
    tempV = n - v
else:
    tempV = v

print(tempH * tempV * 4)