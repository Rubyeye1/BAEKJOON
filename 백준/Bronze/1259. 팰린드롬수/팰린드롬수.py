import math
import sys
from collections import deque
import copy
import datetime

while True:
    L = input()

    if L == "0":
        break

    reverseL = L[::-1]

    if L == reverseL:
        print("yes")
    else:
        print("no")