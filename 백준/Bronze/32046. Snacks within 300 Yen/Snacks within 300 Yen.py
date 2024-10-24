import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime



while True:
    N = int(sys.stdin.readline())
    if N == 0:
        break

    L = list(map(int, sys.stdin.readline().split()))

    result = 0

    for i in range(len(L)):
        result += L[i]
        if result > 300:
            result -= L[i]

    print(result)