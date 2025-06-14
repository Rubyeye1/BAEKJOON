import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

x = int(sys.stdin.readline())
makdae = 64
cnt = 0

while x > 0:
    if makdae > x:
        makdae //= 2
    else:
        x -= makdae
        cnt += 1

print(cnt)