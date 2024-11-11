import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

L = input()
L = list(L)

temp1 = 0
temp2 = 0

for i in range(len(L)):
    if L[i] == "+":
        temp1 = i
    if L[i] == "=":
        temp2 = i

a = int(L[temp1-2])
b = int(L[temp2-2])
c = int(L[temp2+2])

if a + b == c:
    print("YES")
else:
    print("NO")