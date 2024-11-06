import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

k = int(sys.stdin.readline())
temp = 0.01 * k + 25

if temp <= 100:
    print("100.00")
elif temp >= 2000:
    print("2000.00")
else:
    print("{:.2f}".format(temp))