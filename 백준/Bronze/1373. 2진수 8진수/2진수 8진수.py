import math
import sys
from collections import deque
import copy
import datetime

N = str(sys.stdin.readline())

print(oct(int(N, 2))[2:])