import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

N = int(sys.stdin.readline())

if N <= 32767 and N >= -32768:
    print("short")
elif N <= 2147483647 and N >= -2147483648:
    print("int")
else:
    print("long long")