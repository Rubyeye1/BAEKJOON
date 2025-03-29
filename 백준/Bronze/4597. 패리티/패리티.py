import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

while True:

    L = input()

    if L == "#":
        break

    P = L[-1]
    L = L[:-1]

    OneCnt = L.count("1")

    if P == "e":
        if OneCnt % 2 == 0:
            L += "0"
        else:
            L += "1"
            
    else:
        if OneCnt % 2 == 1:
            L += "0"
        else:
            L += "1"
    
    print(L)