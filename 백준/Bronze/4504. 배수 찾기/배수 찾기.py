import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

N = int(sys.stdin.readline())

while True:
    temp = int(sys.stdin.readline())

    if temp == 0:
        break
    if temp % N == 0:
        print("{} is a multiple of {}.".format(temp, N))
    else:
        print("{} is NOT a multiple of {}.".format(temp, N))