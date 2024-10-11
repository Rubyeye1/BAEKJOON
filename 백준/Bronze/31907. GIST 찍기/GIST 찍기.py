import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

K = int(sys.stdin.readline())

for i in range(K):
    print("G" * K + "..." * K)
for i in range(K):
    print("." * K + "I" * K + "." * K + "T" * K)
for i in range(K):
    print(".." * K + "S" * K + "." * K)