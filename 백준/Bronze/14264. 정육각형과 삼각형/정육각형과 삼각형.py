import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

L = int(sys.stdin.readline())

result = (L ** 2) * math.sqrt(3) / 4

print(result)