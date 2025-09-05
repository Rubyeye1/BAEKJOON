import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
A.sort()

print(A[-1])