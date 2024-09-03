import math
import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

N, W, H = map(int, sys.stdin.readline().split())
result = math.sqrt(W * W + H * H)

for i in range(N):

    temp = int(sys.stdin.readline())

    if temp <= result:
        print("DA")
    else:
        print("NE")