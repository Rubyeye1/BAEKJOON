import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

while True:
    
    try:
        n, k = map(int, sys.stdin.readline().split())
        temp = n

        while n // k != 0:
            temp += n // k
            n = n // k + n % k

        print(temp)

    except:
        break