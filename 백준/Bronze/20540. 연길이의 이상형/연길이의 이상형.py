import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

y = input()
b = []

if y[0] == 'E':
    b.append('I')
elif y[0] == 'I':
    b.append('E')
if y[1] == 'S':
    b.append('N')
elif y[1] == 'N':
    b.append('S')
if y[2] == 'T':
    b.append('F')
elif y[2] == 'F':
    b.append('T')
if y[3] == 'J':
    b.append('P')
elif y[3] == 'P':
    b.append('J')

for i in range(len(b)):
    print(b[i], end="")