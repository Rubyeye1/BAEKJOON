import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

n = int(sys.stdin.readline())

for _ in range(n):

    L = input()
    L = list(L)

    result = 0
    temp = 23

    for i in range(len(L)):

        if L[i] == "1":
            result += 2 ** temp

        temp -= 1

    print(result)