import math
import sys
from collections import deque
import copy
import datetime


a, b = map(int, sys.stdin.readline().split())
temp = b-a
Max = temp

for i in range(3):
    Out, In = map(int,sys.stdin.readline().split())

    temp = temp + (In-Out)

    if Max < temp:
        Max = temp


print(Max)