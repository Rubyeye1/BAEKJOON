import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

A = input()
B = input()
temp = input()

if temp in A and temp in B:
    print("YES")
else:
    print("NO")