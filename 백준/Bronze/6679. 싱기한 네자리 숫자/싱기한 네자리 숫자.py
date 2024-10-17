import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

for i in range(2992, 10000):
    
    N = i
    temp = 0

    while N != 0:
        temp += N % 10
        N //= 10

    N = i
    temp12 = 0

    while N != 0:
        temp12 += N % 12
        N //= 12

    N = i
    temp16 = 0

    while N != 0:
        temp16 += N % 16
        N //= 16

    if temp == temp12 == temp16:
        print(i)