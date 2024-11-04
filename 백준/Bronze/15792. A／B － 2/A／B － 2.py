import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime


a, b = map(int, sys.stdin.readline().split())
print(str(a//b) + ".", end="")

for i in range(1000):
    a = (a % b) * 10
    print(a//b, end="")