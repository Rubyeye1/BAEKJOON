import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime


k = int(sys.stdin.readline())
k = list(map(int, str(k)))

k.sort(reverse=True)
k = list(map(int, k))
for i in range(len(k)):
    print(k[i], end="")