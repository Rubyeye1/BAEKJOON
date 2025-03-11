import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

while True:

    N = int(sys.stdin.readline())
    if N == 0:
        break

    temp = list(map(int, str(N)))

    while True:

        result = 0
        for i in range(len(temp)):
            result += temp[i]

        if result <= 9:
            break

        temp = list(map(int, str(result)))

    print(result)