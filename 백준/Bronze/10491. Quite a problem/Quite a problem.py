import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime


while True:
    try:
        a = input()
        a = a.lower()

        if "problem" in a:
            print("yes")
        else:
            print("no")
            
    except EOFError:
        break