import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

N = int(sys.stdin.readline())

Jayeon = 1
result = 0

while True:
    if Jayeon > N:
        Jayeon = 1

    N -= Jayeon
    Jayeon += 1
    result += 1

    if N <= 0:
        break

print(result)