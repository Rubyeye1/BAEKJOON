import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

T = int(sys.stdin.readline())

for i in range(T):
    a, b = map(int, sys.stdin.readline().split())
    temp1 = int(b / 7)
    temp2 = int(b / 4)
    print(a - temp1 + temp2)
