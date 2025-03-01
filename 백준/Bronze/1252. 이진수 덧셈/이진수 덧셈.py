import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re


A, B = map(str, sys.stdin.readline().split())
A = int(A, 2)
B = int(B, 2)

print(bin(A+B)[2:])