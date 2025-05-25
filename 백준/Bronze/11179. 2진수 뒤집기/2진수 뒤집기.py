import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

N = int(sys.stdin.readline())
L = bin(N)
L = L[2:]
L = L[::-1]

print(int(L, 2))