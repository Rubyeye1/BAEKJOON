import math
import sys
from collections import deque
import copy
import datetime

N = int(sys.stdin.readline())
result = 0
for i in range(N):
    a, b, c = map(int, sys.stdin.readline().split())
    temp = 0
    if a==b==c:
        temp = 10000 + a * 1000
    elif a==b!=c:
        temp = 1000 + a * 100
    elif a==c!=b:
        temp = 1000 + a * 100
    elif c==b!=a:
        temp = 1000 + c * 100
    elif a!=b!=c:
        temp = max(a,b,c) * 100

    if result < temp:
        result = temp

print(result)