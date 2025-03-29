import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

t = int(sys.stdin.readline())

for _ in range(t):
    
    n = int(sys.stdin.readline())

    temp = 1

    for i in range(1, n+1):

        temp *= i

        while (temp % 10 == 0):
            temp = temp / 10
        
        temp %= 10000000
    
    print(int(temp%10))