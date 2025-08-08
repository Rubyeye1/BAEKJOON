import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

K, N = map(int, sys.stdin.readline().split())

if N == 1:
    print(-1)
    
else:
    temp = (K * N) // (N - 1)

    if (K * N) % (N - 1):
        temp += 1 

    print(temp)