import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

S = input()
result = 0
temp = 0

for i in range(len(S)):
    
    if S[i] == "K" and temp == 0:
        temp += 1
        result += 1
    elif S[i] == "O" and temp == 1:
        temp += 1
        result += 1
    elif S[i] == "R" and temp == 2:
        temp += 1
        result += 1
    elif S[i] == "E" and temp == 3:
        temp += 1
        result += 1
    elif S[i] == "A" and temp == 4:
        temp = 0
        result += 1

print(result)