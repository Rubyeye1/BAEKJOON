import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

e, f, c = map(int, sys.stdin.readline().split())
hap = e + f
result = 0

while True:
    tempM = hap // c
    tempN = hap % c
    result += tempM
    
    if tempM == 0:
        break
        
    hap = tempM + tempN

print(result)