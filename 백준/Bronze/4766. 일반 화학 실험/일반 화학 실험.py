import math
import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

a = float(sys.stdin.readline())
b = float(sys.stdin.readline())
result = b
print("{:.2f}".format(b-a))

while True:
    
    temp = float(sys.stdin.readline())
    if temp == 999:
        break
        
    result = temp - result
    print("{:.2f}".format(result))
    
    result = temp