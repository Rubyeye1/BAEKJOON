import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

L = input()
L = list(L)
for i in range(len(L)):
    L[i] = int(L[i])

result = 2 * L[0] + 7 * L[1] + 6 * L[2] + 5 * L[3] + 4 * L[4] + 3 * L[5] + 2 * L[6]
result %= 11

if result == 0:
    print("J")
elif result == 1:
    print("A")
elif result == 2:
    print("B")
elif result == 3:
    print("C")
elif result == 4:
    print("D")
elif result == 5:
    print("E")
elif result == 6:
    print("F")
elif result == 7:
    print("G")
elif result == 8:
    print("H")
elif result == 9:
    print("I")
elif result == 10:
    print("Z")