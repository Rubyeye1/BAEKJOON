import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

N = int(sys.stdin.readline())

for _ in range(N):
    temp = input()

    if temp[:10] == "Simon says":
        print(temp[10:])