import math
import sys
from collections import deque
import copy
import datetime

a, b = map(int, sys.stdin.readline().split())
print((a+b) * (a-b))