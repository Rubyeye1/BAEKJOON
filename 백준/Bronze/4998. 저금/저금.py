import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

while True:
    try:
        N, B, M = map(float, input().split())
        result = 0

        while M > N:
            N += N * (B / 100)
            result += 1
        print(result)

    except:
        break