import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())

temp = a+b

if temp / 100 >= 1:
    print(3)
elif temp / 10 >= 1:
    print(2)
else:
    print(1)