import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

N = int(sys.stdin.readline())

if N == 1:
    print("int a;")
    print("int *ptr = &a;")
else:
    print("int a;")
    print("int *ptr = &a;")
    print("int **ptr2 = &ptr;")
    for i in range(3, N + 1):
        print("int " + "*" * i + "ptr" + str(i) + " = &ptr" + str(i - 1) + ";")