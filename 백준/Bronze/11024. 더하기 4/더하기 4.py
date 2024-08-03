import math
import sys
from collections import deque
import copy
import datetime

T = int(sys.stdin.readline())

for i in range(T):
    L = list(map(int, sys.stdin.readline().split()))
    
    result = 0
    
    for j in range(len(L)):
        result += L[j]
    
    print(result)