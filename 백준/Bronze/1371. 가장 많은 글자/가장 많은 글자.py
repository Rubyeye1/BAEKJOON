import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

L = sys.stdin.read()

temp = [0] * 26

for i in L:
    if i.islower():
        temp[ord(i) - 97] += 1

for i in range(26):
    if temp[i] == max(temp):
        print(chr(97 + i), end='')