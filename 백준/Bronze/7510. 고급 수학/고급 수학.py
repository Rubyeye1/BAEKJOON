import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

n = int(sys.stdin.readline())

for i in range(n):
    L = sorted(map(int, sys.stdin.readline().split()))

    if L[0] ** 2 + L[1] ** 2 == L[2] ** 2:
        print(f"Scenario #{i + 1}:")
        print("yes\n")
    else:
        print(f"Scenario #{i + 1}:")
        print("no\n")