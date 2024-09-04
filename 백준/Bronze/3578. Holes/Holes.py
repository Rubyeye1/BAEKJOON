import math
import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

N = int(sys.stdin.readline())

if N == 0:
    print(1)
    
elif N == 1:
    print(0)
    
else:
    
    if (N % 2) == 1:
        temp = int(N / 2)
        print(4, end="")
        for _ in range(temp):
            print(8, end="")
            
    else:
        temp = int(N / 2)
        for _ in range(temp):
            print(8, end="")