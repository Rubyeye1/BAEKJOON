import math
import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

while True:
    
    try:
        N, S = map(int, sys.stdin.readline().split())
        print(S // (N + 1))
        
    except:
        break