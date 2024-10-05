import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

a = input()
a = list(a)

temp = 0
final = 0

for i in range(len(a)):
    if a[i] == "H" and temp == 0:
        temp += 1
    elif a[i] == "O" and temp == 1:
        temp += 1
    elif a[i] == "N" and temp == 2:
        temp += 1
    elif a[i] == "I" and temp == 3:
        temp += 1

    if temp == 4:
        final += 1
        temp = 0

print(final)