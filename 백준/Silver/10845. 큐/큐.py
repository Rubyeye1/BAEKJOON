import math
import sys
from collections import deque
import copy
import datetime


N = int(sys.stdin.readline())
dq = deque([])


for i in range(N):
    temp = sys.stdin.readline().split()
    if temp[0] == "push":
        dq.append(temp[1])
    elif temp[0] == "pop":
        if len(dq) == 0:
            print("-1")
        else:
            print(dq.popleft())
    elif temp[0] == "size":
        print(len(dq))
    elif temp[0] == "empty":
        if len(dq) == 0:
            print(1)
        else:
            print(0)
    elif temp[0] == "front":
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[0])
    elif temp[0] == "back":
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[-1])