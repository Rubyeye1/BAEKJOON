import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

N = int(sys.stdin.readline())
temp = 1

while True:

    N -= temp
    temp += 1

    if N < 0:

        if temp % 2 == 0:
            print(abs(N))
        else:
            print(0)

        break