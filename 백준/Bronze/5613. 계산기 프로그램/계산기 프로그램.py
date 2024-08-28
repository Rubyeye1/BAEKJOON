import math
import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

temp = int(sys.stdin.readline())

while True:
    
    M = input()
    
    if M == "=":
        print(int(temp))
        break
        
    N = int(sys.stdin.readline())

    if M == "+":
        temp += N
    elif M == "-":
        temp -= N
    elif M == "*":
        temp *= N
    elif M == "/":
        temp /= N
        temp = math.floor(temp)