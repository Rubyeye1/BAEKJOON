import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

A, B = map(int, sys.stdin.readline().split())
C, D = map(int, sys.stdin.readline().split())

L = [A / C + B / D, C / D + A / B, D / B + C / A, B / A + D / C]

print(L.index(max(L)))