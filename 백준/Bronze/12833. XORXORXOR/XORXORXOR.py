import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

A, B, C = map(int, sys.stdin.readline().split())

for _ in range(C % 2):
    A ^= B

print(A)