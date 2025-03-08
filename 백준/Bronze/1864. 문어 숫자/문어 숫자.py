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

    result = 0

    for i in range(len(L)):
        if L[i] == "~":
            continue
        elif L[i] == "\\":
            result += 8 ** (len(L)-1 - i) * 1
        elif L[i] == "(":
            result += 8 ** (len(L)-1 - i) * 2
        elif L[i] == "@":
            result += 8 ** (len(L)-1 - i) * 3
        elif L[i] == "?":
            result += 8 ** (len(L)-1 - i) * 4
        elif L[i] == ">":
            result += 8 ** (len(L)-1 - i) * 5
        elif L[i] == "&":
            result += 8 ** (len(L)-1 - i) * 6
        elif L[i] == "%":
            result += 8 ** (len(L)-1 - i) * 7
        elif L[i] == "/":
            result += 8 ** (len(L)-1 - i) * (-1)

    print(result)