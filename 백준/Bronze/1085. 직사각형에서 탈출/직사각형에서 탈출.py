import math
import sys
from collections import deque
import copy
import datetime

x, y, w, h = map(int, sys.stdin.readline().split())

print(min(x, y, w-x, h-y))