import math
import sys
from collections import deque
import copy
import datetime

a = int(input())
temp = 0
standard = 2 ** 30
while True:
    if 2 ** temp == a:
        print(1)
        break
    elif 2 ** temp > standard:
        print(0)
        break
    else:
        temp = temp + 1