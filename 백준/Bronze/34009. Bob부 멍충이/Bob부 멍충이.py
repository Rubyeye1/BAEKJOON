import sys
from collections import deque
import copy
import datetime
from datetime import date, datetime
import re
import math

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

if N % 2 == 0:
    print("Alice")
else:    
    print("Bob")