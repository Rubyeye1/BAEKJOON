import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

N = int(sys.stdin.readline())
L = list(map(int, sys.stdin.readline().split()))
L.sort()

print(L[-1] - L[0])