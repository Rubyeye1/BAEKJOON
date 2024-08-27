import math
import sys
from collections import deque
import copy
import datetime
from datetime import date, datetime


L = list(map(int, sys.stdin.readline().split()))
L.sort()

temp = input()

if temp == "ABC":
    print(L[0], L[1], L[2])
elif temp == "ACB":
    print(L[0], L[2], L[1])
elif temp == "BAC":
    print(L[1], L[0], L[2])
elif temp == "BCA":
    print(L[1], L[2], L[0])
elif temp == "CAB":
    print(L[2], L[0], L[1])
elif temp == "CBA":
    print(L[2], L[1], L[0])