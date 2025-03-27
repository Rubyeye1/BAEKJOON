import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

N = input()
L = ''

for i in range(1, 100001):
    L = L + str(i)

print(L.index(N) + 1)