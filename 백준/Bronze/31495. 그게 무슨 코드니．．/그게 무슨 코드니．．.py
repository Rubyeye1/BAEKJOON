import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

L = input()
L = list(L)

if L[0] == "\"" and L[-1] == "\"" and len(L) >= 3:
    for i in range(1, len(L)-1):
        print(L[i], end="")
elif L[0] == "\"" and L[-1] == "\"" and len(L) <= 2:
    print("CE")
elif L[0] == "\"" and len(L) == 1:
    print("CE")
else:
    print("CE")