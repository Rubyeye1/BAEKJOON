import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

S = input()
S = list(S)
A = 0
B = 0

for i in range(0, len(S), 2):
    if S[i] == "A":
        A += int(S[i+1])
    elif S[i] == "B":
        B += int(S[i+1])

if A > B:
    print("A")
else:
    print("B")