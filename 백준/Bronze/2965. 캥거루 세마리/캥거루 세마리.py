import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

A, B, C = map(int, sys.stdin.readline().split())

temp = max(B - A, C - B)
temp -= 1
print(temp)