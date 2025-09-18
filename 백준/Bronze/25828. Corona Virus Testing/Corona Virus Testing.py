import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

g, p, t = map(int, sys.stdin.readline().split())
temp1 = g * p
temp2 = g + p * t

if temp1 < temp2:
    print(1)
elif temp1 > temp2:
    print(2)
else:
    print(0)