import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

A, B = map(int, sys.stdin.readline().split())
C = int(sys.stdin.readline())

if A + B >= 2 * C:
    print(A + B - (2 * C))
else:
    print(A + B)