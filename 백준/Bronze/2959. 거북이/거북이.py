import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

L = list(map(int, sys.stdin.readline().split()))
L.sort()

print(L[0] * L[2])