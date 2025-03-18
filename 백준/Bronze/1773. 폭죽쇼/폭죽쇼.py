import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

N, C = map(int, sys.stdin.readline().split())
L = [0] * (C + 1)
result = 0

for _ in range(N):

    temp = int(sys.stdin.readline())

    for i in range(temp, C+1, temp):

        if L[i] != 1:
            
            L[i] = 1
            result += 1

print(result)