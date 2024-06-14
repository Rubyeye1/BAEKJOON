import math
import sys
from collections import deque
import copy
import datetime

S, T, D = map(int, sys.stdin.readline().split())
print(D // (S * 2) * T)