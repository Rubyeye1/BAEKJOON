import math
import sys
from collections import deque
import copy
import datetime

Hour1, Minute1, Second1 = map(int, sys.stdin.readline().split(':'))
Hour2, Minute2, Second2 = map(int, sys.stdin.readline().split(':'))

temp = (Hour2 * 3600) + (Minute2 * 60) + Second2 - ((Hour1 * 3600) + (Minute1 * 60) + Second1)

if temp < 0:
    temp += 60 * 60 * 24

ResultHour = temp // 3600
ResultMinute = (temp % 3600) // 60
ResultSecond = temp % 60

print("%02d:%02d:%02d" % (ResultHour, ResultMinute, ResultSecond))