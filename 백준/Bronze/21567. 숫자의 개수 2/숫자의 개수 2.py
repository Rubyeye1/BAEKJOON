import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

L = [0] * 10
result = 1

for i in range(3):
    temp = int(input())
    result *= temp

for i in str(result):
    L[int(i)] += 1

for i in range(len(L)):
    print(L[i])