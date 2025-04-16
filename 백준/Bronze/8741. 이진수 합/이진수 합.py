import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

k = int(sys.stdin.readline())
k = (2 ** k) - 1

temp = k * (k+1) // 2
temp = bin(temp)[2:]

print(temp)