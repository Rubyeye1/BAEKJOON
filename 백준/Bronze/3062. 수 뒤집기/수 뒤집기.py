import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

T = int(sys.stdin.readline())

for _ in range(T):
    N = input()
    temp = str(int(N) + int(N[::-1]))

    if temp == temp[::-1]:
        print("YES")
    else:
        print("NO")