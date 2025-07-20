import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

N = input()
chk = 0

for i in range(1, len(N)):
    L1, L2 = N[:i], N[i:]
    temp1 = 1
    temp2 = 1

    for j in L1:
        temp1 *= int(j)
    for k in L2:
        temp2 *= int(k)

    if temp1 == temp2:
        chk = 1
        break

if chk == 1:
    print("YES")
else:
    print("NO")