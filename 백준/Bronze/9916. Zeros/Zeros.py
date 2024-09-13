import math
import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

n = int(sys.stdin.readline())
n = math.factorial(n)

print(str(n).count("0"))