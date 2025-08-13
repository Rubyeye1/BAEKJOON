import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

N = int(sys.stdin.readline())
weather = list(map(int, sys.stdin.readline().split()))
L = [0] * N 
temp = 0

for i in range(N):
    if weather[i] == 1:
        temp += 1
    elif weather[i] == 0:
        temp -= 1

    L[i] = temp

print(sum(L))