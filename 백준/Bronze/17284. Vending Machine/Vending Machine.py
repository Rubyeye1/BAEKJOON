import sys
from collections import deque
import copy
import datetime
from datetime import date, datetime
import re
import math

L = map(int, sys.stdin.readline().split())

temp = 5000

for i in L:
    if i == 1:
        temp -= 500
    elif i == 2:
        temp -= 800
    else:
        temp -= 1000

print(temp)