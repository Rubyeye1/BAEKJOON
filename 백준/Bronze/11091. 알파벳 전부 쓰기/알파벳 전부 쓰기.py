import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

N = int(sys.stdin.readline())

for _ in range(N):
    L = input().lower()

    RESULT = [0] * 26

    for i in range(len(L)):
        temp = ord(L[i]) - 97

        if temp >= 0 and temp <= 25:
            RESULT[temp] = 1
    
    check = 0

    for i in range(len(RESULT)):
        if RESULT[i] == 1:
            check += 1
    
    if check == 26:
        print("pangram")
    else:
        print("missing", end=" ")

        for i in range(len(RESULT)):
            if RESULT[i] == 0:
                print(chr(i + 97), end="")
        
        print()