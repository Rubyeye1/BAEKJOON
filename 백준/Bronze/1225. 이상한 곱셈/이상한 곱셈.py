import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re


A, B = map(int, sys.stdin.readline().split())
A = list(map(int, str(A)))
B = list(map(int, str(B)))

print(sum(A) * sum(B))