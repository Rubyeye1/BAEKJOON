import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

c, b = map(int, sys.stdin.readline().split())

if c % b == 0:
    print(int(c / b))
else:
    print("%.10f" % (c / b))