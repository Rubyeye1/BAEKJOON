import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

N = int(sys.stdin.readline())

for _ in range(N):
    temp = int(sys.stdin.readline())

    if temp % 2:
        print('odd')
    else:
        print('even')