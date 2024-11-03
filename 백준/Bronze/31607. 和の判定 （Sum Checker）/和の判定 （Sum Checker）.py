import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime


a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())
L = [a,b,c]

L.sort()

if L[0]+L[1] == L[2]:
    print(1)
else:
    print(0)