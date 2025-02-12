import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

a, b = map(int, sys.stdin.readline().split())

print(math.sqrt(a ** 2 + b ** 2))