import math
import sys
from collections import deque
import copy

L = [0] * 46
L[1] = 1

for i in range(1, 45):
    L[i+1] = L[i-1] + L[i]
    
n = int(sys.stdin.readline())
print(L[n])
