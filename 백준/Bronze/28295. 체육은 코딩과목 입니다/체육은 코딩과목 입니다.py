import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

result = 0

for _ in range(10):
    temp = int(sys.stdin.readline())

    if temp == 1:
        result += 90
    elif temp == 2:
        result += 180
    elif temp == 3:
        result -= 90

result %= 360

if result == 0:
    print("N")
elif result == 90:
    print("E")
elif result == 180:
    print("S")
elif result == 270:
    print("W")