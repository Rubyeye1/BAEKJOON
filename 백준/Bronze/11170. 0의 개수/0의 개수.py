import math
import sys
from collections import deque
import copy
import datetime

T = int(sys.stdin.readline())

for i in range(T):

    result = 0
    N, M = map(int, sys.stdin.readline().split())

    for j in range(N, M+1, 1):
        StrJ = str(j)
        result += StrJ.count('0')

    print(result)