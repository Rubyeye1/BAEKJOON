import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

n = int(sys.stdin.readline())

for _ in range(n):

    L = input()
    temp = 0

    for i in range(len(L)):

        if L[i] == "G" or L[i] == "g":
            temp += 1

        elif L[i] == "B" or L[i] == "b":
            temp -= 1
    
    if temp > 0:
        print(L + " is GOOD")
    elif temp == 0:
        print(L + " is NEUTRAL")
    elif temp <0:
        print(L + " is A BADDY")    