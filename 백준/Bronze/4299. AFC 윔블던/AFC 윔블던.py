import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

h, c = map(int, sys.stdin.readline().split())

if h < c:
    print(-1)
else:
    a = (h + c) // 2
    b = (h - c) // 2

    if a + b == h and a - b == c: 
        print(a, b)
    else:
        print(-1)