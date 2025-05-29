import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

a = input()
result = ""

for i in a:
    if i == 'A' or i == 'B' or i == 'C':
        result += chr(ord(i) + 23)
    else:
        result += chr(ord(i) - 3)

print(result)