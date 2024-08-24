import math
import sys
from collections import deque
import copy
import datetime
from datetime import date, datetime


N, M = map(int, sys.stdin.readline().split())

for i in range(N):
    temp = input()
    print(temp[::-1])