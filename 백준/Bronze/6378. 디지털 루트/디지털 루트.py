import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

while True:
    N = input()
    
    if N == '0':
        break
    
    while True:
        N = sum(list(map(int, str(N))))
        
        if (N // 10) == 0:
            print(N)
            break