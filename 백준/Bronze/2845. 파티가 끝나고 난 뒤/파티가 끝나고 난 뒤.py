import math
import sys
from collections import deque
import copy
import datetime

L, P = map(int, sys.stdin.readline().split())
A,B,C,D,E= map(int, sys.stdin.readline().split())

temp = L * P
print(A-temp, B-temp, C-temp, D-temp, E-temp)