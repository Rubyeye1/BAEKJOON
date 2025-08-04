import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

Case = 1

while True:
    a, ysj, b=input().strip().split()

    if ysj =="E":
        break
    if ysj =="!=":
        print("Case {}: ".format(Case) + str(int(a) != int(b)).lower())
    elif ysj ==">":
        print("Case {}: ".format(Case) + str(int(a) > int(b)).lower())
    elif ysj =="<":
        print("Case {}: ".format(Case) + str(int(a) < int(b)).lower())
    elif ysj ==">=":
        print("Case {}: ".format(Case) + str(int(a) >= int(b)).lower())
    elif ysj =="<=":
        print("Case {}: ".format(Case) + str(int(a) <= int(b)).lower())
    elif ysj =="==":
        print("Case {}: ".format(Case) + str(int(a) == int(b)).lower())

    Case += 1