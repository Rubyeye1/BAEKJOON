import math
import sys
from collections import deque
import copy
import datetime
from datetime import date, datetime


A, B = map(int, sys.stdin.readline().split())
C, D = map(int, sys.stdin.readline().split())

if A+D >= B+C:
    print(B+C)
elif B+C >= A+D:
    print(A+D)
else:
    print(B+C)