import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())

    if n > 2:
        print(3)
    else:
        print(1)