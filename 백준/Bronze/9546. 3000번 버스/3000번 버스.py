import math
import sys
from collections import deque
import copy
import datetime
from datetime import date, datetime


T = int(sys.stdin.readline())

for i in range(T):
    
    k = int(sys.stdin.readline())
    print(2 ** k - 1)