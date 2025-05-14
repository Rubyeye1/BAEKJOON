import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

A, B = map(int, sys.stdin.readline().split())

print(max(A + B, A - B))
print(min(A + B, A - B))