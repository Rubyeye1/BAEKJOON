import sys
from collections import deque
import copy
import datetime
from datetime import date, datetime
import re
import math

T = int(sys.stdin.readline())

for i in range(T):
    N = int(sys.stdin.readline())
    L = list(map(int, sys.stdin.readline().split()))
    
    print(min(L),max(L))