import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

S = input()
K = input()
temp = ''

for i in range(len(S)):
    if S[i].isalpha():
        temp += S[i] 

if K in temp:
    print(1)
else:
    print(0)