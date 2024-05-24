import math
import sys
from collections import deque
import copy
import datetime


N = int(sys.stdin.readline())
L = []
for i in range(N):
    temp = input()
    L.append(temp)

for i in range(N):
    print(str(i+1) + ". " + L[i])