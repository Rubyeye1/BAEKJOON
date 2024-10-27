import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

while True:

    l, w, h, v = map(int, sys.stdin.readline().split())
    if l == 0 and w == 0 and h == 0 and v == 0:
        break

    if l == 0:
        l = v / (w * h)
        l = int(l)
    elif w == 0:
        w = v / (l * h)
        w = int(w)
    elif h == 0:
        h = v / (l * w)
        h = int(h)
    elif v == 0:
        v = l * w * h

    print(l, w, h, v)