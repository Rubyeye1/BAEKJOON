import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

N = int(sys.stdin.readline())

while True:
    chk = 0

    for i in str(N):
        if i !="4" and i !="7":
            chk = 1
            N -=1
    
    if chk == 0:
        break
print(N)