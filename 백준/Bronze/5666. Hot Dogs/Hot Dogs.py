import math
import sys
from collections import deque
import copy
import datetime
from datetime import date, datetime

try:
    while True:
        H, P = map(int, sys.stdin.readline().split())
        temp = H / P
        result = f"{temp:.2f}"
        print(result)

except:
    exit()