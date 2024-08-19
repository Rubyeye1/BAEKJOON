import math
import sys
from collections import deque
import copy
import datetime
from datetime import date, datetime


N = int(sys.stdin.readline())
L = []

for i in range(N):
    temp = input()
    L.append(temp)

if "anj" in L:
    print("뭐야;")
else:
    print("뭐야?")