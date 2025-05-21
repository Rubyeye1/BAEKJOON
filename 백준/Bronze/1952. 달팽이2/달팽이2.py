import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

M, N = map(int, sys.stdin.readline().split())

if M > N:
    print(N * 2 - 1)
else:
    print(M * 2 - 2)