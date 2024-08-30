import math
import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

a = input()
result = 0

if "M" in a:
    result += 1
if "O" in a:
    result += 1
if "B" in a:
    result += 1
if "I" in a:
    result += 1
if "S" in a:
    result += 1

if result == 5:
    print("YES")
else:
    print("NO")