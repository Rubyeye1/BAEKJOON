import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

T = int(sys.stdin.readline())

for i in range(T):
    
    d = int(sys.stdin.readline())
    temp = 0
    
    while True:
        m = temp + temp * temp
        
        if m <= d:
            temp += 1
        else:
            temp -= 1
            break
            
    print(temp)