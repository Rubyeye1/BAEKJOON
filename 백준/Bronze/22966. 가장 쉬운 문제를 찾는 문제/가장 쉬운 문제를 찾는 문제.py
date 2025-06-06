import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

N = int(sys.stdin.readline())
zL = []
nanL = []

for _ in range(N):
    z, nan = input().split()

    zL.append(z)
    nanL.append(int(nan))

for i in range(N):
    if nanL[i] == min(nanL):
        print(zL[i])