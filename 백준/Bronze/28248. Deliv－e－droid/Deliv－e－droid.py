import math
import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

x = int(sys.stdin.readline())
y = int(sys.stdin.readline())
if x > y:
    print(x * 50 - y * 10 + 500)
else:
    print(x * 50 - y * 10)