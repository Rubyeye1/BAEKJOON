import math
import sys
from collections import deque
import copy
import datetime

A_A, A_E = map(int, sys.stdin.readline().split())
B_A, B_E = map(int, sys.stdin.readline().split())

while True:
    A_E -= B_A
    B_E -= A_A

    if A_E <= 0 and B_E <= 0:
        print("DRAW")
        break
    elif A_E <= 0:
        print("PLAYER B")
        break
    elif B_E <= 0:
        print("PLAYER A")
        break