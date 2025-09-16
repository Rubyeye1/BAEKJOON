import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

N = input()
L = '1' * len(N)

if len(N) == 1:
    print(1)
elif int(N) >= int(L):
    print(len(N))
else:
    print(len(N) - 1)