import math
import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

T = int(sys.stdin.readline())
L = []

for _ in range(T):
    
    a, b = map(int, sys.stdin.readline().split())
    if b == 1:
        L.append(a)

L.sort()

result = 0

for i in range(len(L)-1):
    if L[i+1] - L[i] > result:
        result = L[i+1] - L[i]

print(result)