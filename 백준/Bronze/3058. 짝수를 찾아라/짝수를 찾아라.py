import math
import sys
from collections import deque
import copy
import datetime

T = int(sys.stdin.readline())

for i in range(T):
    
    result = []
    temp = list(map(int,sys.stdin.readline().split()))
    
    for j in range(len(temp)):
        if (temp[j] % 2) == 0:
            result.append(temp[j])
            
    print(sum(result), min(result))