import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

N = int(sys.stdin.readline())
for i in range(N):
    a, b = map(str, input().split())
    a = int(a)

    for j in range(a):
        print(b, end="")
    print()