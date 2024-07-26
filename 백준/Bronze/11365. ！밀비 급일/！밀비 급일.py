import math
import sys
from collections import deque
import copy
import datetime

a = []

while True:

    b = sys.stdin.readline().strip()

    if b == "END":
        break

    a.append(b)

for i in range(len(a)):
    print(a[i][::-1])