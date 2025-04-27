import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

k, c = map(str, sys.stdin.readline().split())
temp = int(c + k)
check1 = 0
check2 = 0

for i in range(2, int(math.sqrt(int(k))) + 1):
    if int(k) % i == 0:
        check1 = 1
        break
for i in range(2, int(math.sqrt(temp)) + 1):
    if temp % i == 0:
        check2 = 1
        break

if check1 == 0 and check2 == 0:
    print("Yes")
else:
    print("No")