import math
import sys
from collections import deque
import copy
import datetime

N = int(sys.stdin.readline())
for i in range(N):
    L = list(map(str, input().split()))
    for j in range(len(L)):
        temp = list(L[j])
        for k in range(len(temp)-1, -1, -1):
            print(temp[k], end="")
        print(" ", end="")
    print("")