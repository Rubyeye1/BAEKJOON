import math
import sys
from collections import deque
import copy
import datetime

L = list(map(int, sys.stdin.readline().split()))
L.sort()

if L[0] + L[1] <= L[2]:
    L[2] = L[0] + L[1] - 1
    
print(L[0] + L[1] + L[2])