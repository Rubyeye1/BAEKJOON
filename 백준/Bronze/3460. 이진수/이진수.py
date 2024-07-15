import math
import sys
from collections import deque
import copy
import datetime

T = int(sys.stdin.readline())

for _ in range(T):
    temp = bin(int(sys.stdin.readline()))[2:]


    for i in range(len(temp)):
        if temp[-1-i] == '1':
            print(i, end =" ")