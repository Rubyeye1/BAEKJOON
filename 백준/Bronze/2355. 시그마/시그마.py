import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

A, B = map(int, sys.stdin.readline().split())

if A > B:
    temp = A
    A = B
    B = temp

result = B * (B + 1) // 2 - (A * (A - 1) // 2)

print(result)