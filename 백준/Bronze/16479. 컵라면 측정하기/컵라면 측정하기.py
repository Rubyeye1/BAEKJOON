import math
import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

K = int(sys.stdin.readline())
D1, D2 = map(int, sys.stdin.readline().split())
if D1 == D2:
    print(K * K)
else:
    print((K * K) - (abs((D1 - D2) / 2) * abs((D1 - D2) / 2)))