import math
import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

N = int(sys.stdin.readline())
if N == 0 or N == 1:
    print(1)
else:
    result = 1

    while True:
        result *= N
        N -= 1

        if N == 1:
            break

    print(result)