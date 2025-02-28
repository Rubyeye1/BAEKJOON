import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re


K = int(sys.stdin.readline())

for j in range(K):
    
    h = int(sys.stdin.readline())
    T = input()
    
    for i in range(len(T)):
        if T[i] =="c":
            h += 1
        if T[i] == "b":
            h -= 1

    print("Data Set " + str(j+1) + ":")
    print(h)
    print()