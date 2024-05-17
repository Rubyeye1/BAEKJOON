import math
import sys
from collections import deque
import copy
import datetime


N = int(input())
result = 0
for i in range(N+1):
    for j in range(i+1):
        result += i+j

print(result)