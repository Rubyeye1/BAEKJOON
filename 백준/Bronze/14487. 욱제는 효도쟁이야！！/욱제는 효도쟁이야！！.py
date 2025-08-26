import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

n = int(sys.stdin.readline())
L = list(map(int, sys.stdin.readline().split()))

print(sum(L) - max(L))