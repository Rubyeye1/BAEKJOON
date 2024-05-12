import math
import sys
from collections import deque
import copy
import datetime

N = int(input())
L = list(map(int, sys.stdin.readline().split()))

print(max(L)*min(L))