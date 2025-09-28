import sys
from collections import deque
import copy
import datetime
from datetime import date, datetime
import re
import math

N, M = map(int, sys.stdin.readline().split())

if (N * M) % 3 == 0:
    print('YES')
else:
    print('NO')