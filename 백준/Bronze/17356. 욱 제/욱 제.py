import math
import sys
from collections import deque
import copy
import datetime
from datetime import date, datetime


A, B = map(int, sys.stdin.readline().split())

M = (B - A) / 400
result = 1 / (1 + (10 ** M))
print(result)