import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

T = int(sys.stdin.readline())
N = list(map(int, sys.stdin.readline().split()))

for i in N:
    temp = 0
    
    for j in range(1, i):
        if i % j == 0:
            temp += j
    
    if temp > i:
        print("Abundant")
    elif temp < i:
        print("Deficient")
    else:
        print("Perfect")