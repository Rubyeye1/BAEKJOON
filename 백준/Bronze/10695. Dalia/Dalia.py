import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

T = int(sys.stdin.readline())

for i in range(T):
    
    n, r1, c1, r2, c2 = map(int, sys.stdin.readline().split())
    
    if r1-1 == r2 and c1+2 == c2:
        print("Case " + str((i+1)) + ": YES")
    elif r1-1 == r2 and c1-2 == c2:
        print("Case " + str((i+1)) + ": YES")
    elif r1+1 == r2 and c1+2 == c2:
        print("Case " + str((i+1)) + ": YES")
    elif r1+1 == r2 and c1-2 == c2:
        print("Case " + str((i+1)) + ": YES")
    elif r1-2 == r2 and c1+1 == c2:
        print("Case " + str((i+1)) + ": YES")
    elif r1-2 == r2 and c1-1 == c2:
        print("Case " + str((i+1)) + ": YES")
    elif r1+2 == r2 and c1+1 == c2:
        print("Case " + str((i+1)) + ": YES")
    elif r1+2 == r2 and c1-1 == c2:
        print("Case " + str((i+1)) + ": YES")
        
    else:
        print("Case " + str((i+1)) + ": NO")