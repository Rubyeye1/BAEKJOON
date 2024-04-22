import math
import sys
from collections import deque
import copy
import datetime

S = input()
S = list(S)

for i in range(len(S)):
    if S[i].isupper():
        S[i] = S[i].lower()
    else:
        S[i] = S[i].upper()

for i in range(len(S)):
    print(S[i], end='')
