import math
import sys
from collections import deque
import copy
import datetime

T = int(sys.stdin.readline())

for i in range(T):
    a, b = input().split()
    a = int(a, 2)
    b = int(b, 2)
    temp = a + b
    temp = bin(temp)
    print(temp[2:])