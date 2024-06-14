import math
import sys
from collections import deque
import copy
import datetime

result = 0

for i in range(5):
    temp = int(sys.stdin.readline())
    result += temp
    
print(result)