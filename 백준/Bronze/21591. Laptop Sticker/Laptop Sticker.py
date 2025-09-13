import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

wc, hc, ws, hs = map(int, sys.stdin.readline().split())

if wc >= ws + 2 and hc >= hs + 2:
    print(1)
else:
    print(0)