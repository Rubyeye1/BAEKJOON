import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

N = input()
N = list(map(int, N))

if sum(N[:(len(N)//2)]) == sum(N[(len(N)//2):]):
    print("LUCKY")
else:
    print("READY")