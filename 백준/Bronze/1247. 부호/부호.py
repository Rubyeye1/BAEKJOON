import math
import sys
from collections import deque
import copy
import datetime
from datetime import date, datetime


for i in range(3):

    T = int(sys.stdin.readline())
    result = 0

    for j in range(T):
        temp = int(sys.stdin.readline())
        result += temp

    if result == 0:
        print("0")
    elif result > 0:
        print("+")
    else:
        print("-")