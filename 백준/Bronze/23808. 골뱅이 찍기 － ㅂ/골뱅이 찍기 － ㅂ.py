import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

N = int(sys.stdin.readline())

for i in range(N):
    print("@" * N + "   " * N + "@" * N)
    print("@" * N + "   " * N + "@" * N)
for i in range(N):
    print("@@@@@" * N)
for i in range(N):
    print("@" * N + "   " * N + "@" * N)
for i in range(N):
    print("@@@@@" * N)