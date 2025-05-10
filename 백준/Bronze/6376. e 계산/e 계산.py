import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

def factorial(k):
    gunsa = 1

    for i in range(1, k + 1):
        gunsa *= i

    if k != 0:
        return gunsa
    else:
        return 1

print("n e")
print("- -----------")

result = 0

for i in range(10):
    result += 1 / factorial(i)

    if i == 0 or i == 1:
        print(i, int(result))
    elif i == 2:
        print(i, float(result))
    else:
        print(i, "%.9f"%result)