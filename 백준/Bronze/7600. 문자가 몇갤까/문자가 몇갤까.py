import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

while True:

    L = input()

    if L == "#":
        break

    temp = set([])

    for i in range(len(L)):
        if L[i].isalpha():
            temp.add(L[i].lower())
    
    print(len(temp))