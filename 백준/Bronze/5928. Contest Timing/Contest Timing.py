import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

D, H, M = map(int, sys.stdin.readline().split())

temp = (11 * 24 * 60) + (11 * 60) + 11
ipt = (D * 24 * 60) + (H * 60) + M

result = ipt - temp

if result < 0:
    print(-1)
else:
    print(result)