import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

a, m = map(int, sys.stdin.readline().split())

for i in range(1, 50000):
    if (a * i) % m == 1:
        print(i)
        break