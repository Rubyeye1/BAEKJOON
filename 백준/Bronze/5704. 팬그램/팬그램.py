import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

while True:
    L = input()
    if L == "*":
        break

    if "a" not in L or "b" not in L or "c" not in L or "d" not in L or "e" not in L or "f" not in L or "g" not in L or "h" not in L or "i" not in L or "j" not in L or "k" not in L or "l" not in L or "m" not in L or "n" not in L or "o" not in L or "p" not in L or "q" not in L or "r" not in L or "s" not in L or "t" not in L or "u" not in L or "v" not in L or "w" not in L or "x" not in L or "y" not in L or "z" not in L:
        print("N")
    else:
        print("Y")