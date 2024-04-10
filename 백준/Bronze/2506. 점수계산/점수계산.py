import math
import sys
from collections import deque
import copy
import datetime

N = int(input())
L = list(map(int, sys.stdin.readline().split()))
result = 0
count = 0
for i in range(N):
    if L[i] == 1:
        count = count + 1
        result = result + count
    else:
        count = 0

print(result)