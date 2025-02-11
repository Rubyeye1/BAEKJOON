import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

N = int(sys.stdin.readline())

H = list(map(int, sys.stdin.readline().split()))
M = list(map(int, sys.stdin.readline().split()))

result1 = 0
result2 = 0

for i in range(N):
    if M[i] == 0:
        result2 += H[i]
    result1 += H[i]

print(result1)
print(result2)