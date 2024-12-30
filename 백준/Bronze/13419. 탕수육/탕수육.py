import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

T = int(sys.stdin.readline())

for _ in range(T):
    c = input()
    c = list(c)

    if len(c) % 2 == 1:

        for i in range(0, len(c), 2):
            print(c[i], end="")
        for i in range(1, len(c), 2):
            print(c[i], end="")

        print("")

        for i in range(1, len(c), 2):
            print(c[i], end="")
        for i in range(0, len(c), 2):
            print(c[i], end="")

        print("")

    else:
        for i in range(0, len(c), 2):
            print(c[i], end="")

        print("")

        for i in range(1, len(c), 2):
            print(c[i], end="")

        print("")