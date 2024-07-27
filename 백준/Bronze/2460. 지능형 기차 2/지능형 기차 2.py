import math
import sys
from collections import deque
import copy
import datetime

firstOut, firstIn = map(int, sys.stdin.readline().split())

Max = firstIn

for i in range(9):

    tempOut, tempIn = map(int, sys.stdin.readline().split())

    firstIn -= tempOut
    firstIn += tempIn

    if Max < firstIn:
        Max = firstIn

print(Max)