import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

while True:

    S = input()

    if S == "0":
        break

    print(S, end=" ")

    if len(S) == 1:
        continue
    
    else:
        while True:
            temp = 1

            for i in range(len(S)):
                temp *= int(S[i])
            
            print(temp, end=" ")

            S = str(temp)

            if len(S) == 1:
                break