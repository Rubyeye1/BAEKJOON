import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

N = int(sys.stdin.readline())

print(' ' * (N - 1) + '*')
for i in range(N - 1):
    print(' ' * (N - i - 2) + '*' + ' ' * (i * 2 + 1) + '*')