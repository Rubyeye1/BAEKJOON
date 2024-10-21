import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime


a, b = map(int, sys.stdin.readline().split())

b += a
b *= a
b += a
b *= a

print(b)