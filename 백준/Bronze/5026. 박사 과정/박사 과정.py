import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

N  = int(sys.stdin.readline())

for _ in range(N):

    temp = input()

    if temp[0] == "P":
        print("skipped")

    elif temp[0] != "P":
        a, b = map(int, temp.split("+"))
        print(a+b)