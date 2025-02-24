import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

T = int(sys.stdin.readline())

for _ in range(T):
    c, v = map(int, sys.stdin.readline().split())

    you = c // v
    dad = c % v

    print("You get " + str(you) + " piece(s) and your dad gets " + str(dad) + " piece(s).")