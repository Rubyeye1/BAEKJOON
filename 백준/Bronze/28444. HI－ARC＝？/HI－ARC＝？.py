import math
import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

H, I, A, R, C = map(int, sys.stdin.readline().split())

print(H*I - A*R*C)