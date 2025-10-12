import sys
from collections import deque
import copy
import datetime
from datetime import date, datetime
import re
import math

A, B, C = map(int, sys.stdin.readline().split())

if A + B + C > 4:
    print(2)
else:
    print(1)