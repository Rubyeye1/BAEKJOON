import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

T = int(sys.stdin.readline())
N = int(sys.stdin.readline())

F = list(map(int, sys.stdin.readline().split()))
temp = sum(F)

if T <= temp:
    print("Padaeng_i Happy")
else:
    print("Padaeng_i Cry")