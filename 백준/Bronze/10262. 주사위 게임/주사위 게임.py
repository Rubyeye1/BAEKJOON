import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

a1, b1, a2, b2 = map(int, sys.stdin.readline().split())
s1, k1, s2, k2 = map(int, sys.stdin.readline().split())

gun = a1 + b1 + a2 + b2
suk = s1 + k1 + s2 + k2 

if gun > suk:
    print("Gunnar")
elif gun < suk:
    print("Emma")
else:
    print("Tie")