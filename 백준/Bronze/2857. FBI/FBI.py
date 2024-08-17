import math
import sys
from collections import deque
import copy
import datetime
from datetime import date, datetime

result = []

for i in range(5):

    M = input()

    if "FBI" in M:
        result.append(i+1)

if len(result) == 0:
    print("HE GOT AWAY!")
    
else:
    for i in range(len(result)):
        print(result[i], end=" ")