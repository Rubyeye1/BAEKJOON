import math
import sys
from collections import deque
import copy
import datetime

N = int(sys.stdin.readline())
L = []
for i in range(N):

    temp = int(sys.stdin.readline())
    L.append(temp)

result = 0
Max = 0

for i in range(N-1, -1, -1):
    
    if L[i] > Max:
        result += 1
        Max = L[i]

print(result)