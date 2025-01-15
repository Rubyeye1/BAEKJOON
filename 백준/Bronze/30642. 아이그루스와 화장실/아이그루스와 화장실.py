import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

N = int(sys.stdin.readline())
M = input()
K = int(sys.stdin.readline())

if M == "annyong":
    if K % 2 == 1:
        print(K)
    else:
        if K + 1 <= N:
            print(K + 1)
        else:
            print(K - 1)
else:
    if K % 2 == 0:
        print(K)
    else:
        if K + 1 <= N:
            print(K + 1)
        else:
            print(K - 1)