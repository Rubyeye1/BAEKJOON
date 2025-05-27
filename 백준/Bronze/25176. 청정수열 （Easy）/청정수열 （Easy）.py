import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

N = int(sys.stdin.readline())
result = 1

for i in range(1, N + 1):
  result = result * i

print(result)