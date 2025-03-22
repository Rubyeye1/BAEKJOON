import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

N = int(sys.stdin.readline())
L = list(map(int, sys.stdin.readline().split()))
result = []

for i in range(len(L)):
    result.insert(i - L[i],i+1)

for i in range(len(L)):
    print(result[i], end=" ")