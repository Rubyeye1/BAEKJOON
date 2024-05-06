import math
import sys
from collections import deque
import copy
import datetime

L = int(input())
result = 0
while True:
    if L>=5:
        L = L - 5
        result += 1
    elif L > 0 and L < 5:
        result += 1
        break
    else:
        break
print(result)