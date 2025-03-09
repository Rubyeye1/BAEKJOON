import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

a = input()
b = input()
a = list(a)
b = list(b)

i = 0

while True:

    if a[i] in b:
        b.remove(a[i])
        a.remove(a[i])
        i -= 1

    i += 1

    if i >= len(a):
        break

result = len(a) + len(b)

print(result)