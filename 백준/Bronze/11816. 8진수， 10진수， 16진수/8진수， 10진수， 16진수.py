import math
import sys
from collections import deque
import copy
import datetime

L = input()

if L[0] == "0" and L[1] == "x":
    print(int(L, 16))
elif L[0] == "0":
    print(int(L, 8))
else:
    print(L)