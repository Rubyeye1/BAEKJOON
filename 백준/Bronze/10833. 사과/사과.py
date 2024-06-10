import math
import sys
from collections import deque
import copy
import datetime

N = int(sys.stdin.readline())

result = 0

for i in range(N):
    
    a,b = map(int, sys.stdin.readline().split())
    temp = b % a
    result += temp
    
print(result)