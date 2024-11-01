import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

L = list(map(int, sys.stdin.readline().split()))
hong = int(sys.stdin.readline())
hidx = 0

for i in range(len(L)):
    if hong == L[i]:
        hidx = i+1

if hidx >=1 and hidx <=5:
    print("A+")
elif hidx >=6 and hidx <=15:
    print("A0")
elif hidx >=16 and hidx <=30:
    print("B+")
elif hidx >=31 and hidx <=35:
    print("B0")
elif hidx >=36 and hidx <=45:
    print("C+")
elif hidx >=46 and hidx <=48:
    print("C0")
else:
    print("F")