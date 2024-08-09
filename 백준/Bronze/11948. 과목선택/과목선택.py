import math
import sys
from collections import deque
import copy
import datetime
from datetime import date, datetime


Sc = []
So = []

for i in range(4):
    temp = int(sys.stdin.readline())
    Sc.append(temp)
for i in range(2):
    temp = int(sys.stdin.readline())
    So.append(temp)
    
Sc.sort()
So.sort()

result = Sc[1] + Sc[2] + Sc[3] + So[1]
print(result)