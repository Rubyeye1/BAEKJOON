import sys
from collections import deque
import copy
import datetime
from datetime import date, datetime

T = int(sys.stdin.readline())

for i in range(T):
    price = float(input())
    result = f"{round(price*0.8, 2):.2f}"
    print("$" + result)