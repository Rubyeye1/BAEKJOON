import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

N = int(sys.stdin.readline())

for _ in range(N):
    L = list(input().split())

    print(*L[2:], end = " ")
    print(*L[:2])