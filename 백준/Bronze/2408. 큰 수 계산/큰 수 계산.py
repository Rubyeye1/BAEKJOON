import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

N = int(sys.stdin.readline())
L = ''

for _ in range((2 * N) - 1):
    temp = input()

    if temp == "/":
        temp = "//"
        
    L += temp

print(eval(L))