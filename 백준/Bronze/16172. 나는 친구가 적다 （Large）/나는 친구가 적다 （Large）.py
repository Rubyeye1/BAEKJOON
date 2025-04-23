import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

S = input()
K = input()
result = ''

for i in range(len(S)):
    if S[i].isalpha():
        result += S[i]

if K in result:
    print(1)
else:
    print(0)