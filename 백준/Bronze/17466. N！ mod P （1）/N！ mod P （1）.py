import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

N, P = map(int, sys.stdin.readline().split())

temp = 1

for i in range(2, N + 1):
    temp = (temp * i) % P

print(temp % P)