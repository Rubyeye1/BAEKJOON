import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

A, B = map(int, sys.stdin.readline().split())

tempA = 1
tempB = 1

for i in range(B):
    tempA += A - 2
    tempB += tempA

print(tempB)