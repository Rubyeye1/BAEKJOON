import math
import sys
from collections import deque
import copy
import datetime
from datetime import date, datetime
while True:

    temp = int(sys.stdin.readline())
    if temp == 0:
        break

    L = list(map(int, str(temp)))

    result = 0
    result += len(L)-1 + 2

    for i in range(len(L)):
        if L[i] == 1:
            result += 2
        elif L[i] == 0:
            result += 4
        else:
            result += 3

    print(result)