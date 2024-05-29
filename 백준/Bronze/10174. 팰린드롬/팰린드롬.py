import math
import sys
from collections import deque
import copy
import datetime


n = int(sys.stdin.readline())
for i in range(n):

    L = input().lower()
    if (L == L[::-1]):
        print("Yes")
    else:
        print("No")