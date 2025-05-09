import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re


P, K = map(int, sys.stdin.readline().split())
chk = 0

for i in range(2, K):
    if P % i == 0:
        print("BAD", i)
        chk = 1
        break
        
if chk == 0:
    print('GOOD')
