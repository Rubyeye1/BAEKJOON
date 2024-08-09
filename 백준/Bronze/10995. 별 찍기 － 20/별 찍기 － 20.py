import math
import sys
from collections import deque
import copy
import datetime
from datetime import date, datetime


N = int(sys.stdin.readline())

if N == 1:
    print("*")
else:
    for i in range(N):
        if i % 2 == 0:
            print("* " * N)
        else:
            print(" *" * N)