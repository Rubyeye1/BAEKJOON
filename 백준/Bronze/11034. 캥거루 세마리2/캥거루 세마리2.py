import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

while True:
    try:
        A, B, C = map(int, sys.stdin.readline().split())
        print(max(B - A, C - B) - 1)
    except:
        break