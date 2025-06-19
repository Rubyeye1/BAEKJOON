import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

t = int(sys.stdin.readline())

for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())

    print(a+b)
