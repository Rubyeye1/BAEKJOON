import math
import sys
from collections import deque
import copy
import datetime
from datetime import date, datetime


while True:

    temp = input()

    if temp == "#":
        break
        
    result = 0

    for i in range(len(temp)):
        if temp[i] == "a" or temp[i] == "e" or temp[i] == "i" or temp[i] == "o" or temp[i] == "u" or temp[i] == "A" or temp[i] == "E" or temp[i] == "I" or temp[i] == "O" or temp[i] == "U":
            result += 1

    print(result)