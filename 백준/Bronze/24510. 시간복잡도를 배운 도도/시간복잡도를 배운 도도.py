import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

C = int(sys.stdin.readline())
result = 0

for _ in range(C):
    temp = input()

    C1 = temp.count("for")
    C2 = temp.count("while")

    if result < C1 + C2:
        result = C1 + C2

print(result) 