import math
import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

a = input()
cnt = 0

for i in range(len(a)):
    if a[i] == "e":
        cnt += 1

for i in range(len(a)-1):
    print(a[i], end="")

for i in range(cnt):
    print("e", end="")

print(a[-1])