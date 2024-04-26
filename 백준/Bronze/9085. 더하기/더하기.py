import math
import sys
from collections import deque
import copy
import datetime

T = int(sys.stdin.readline())
for i in range(T):
    result = 0
    N = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    for j in range(len(a)):
        result = result + a[j]
    print(result)