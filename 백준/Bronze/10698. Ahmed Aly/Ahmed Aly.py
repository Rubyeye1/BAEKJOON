import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

T = int(sys.stdin.readline())

for j in range(T):
    a = input()
    vmf = 0
    sms = 0

    for i in range(len(a)):
        if a[i] == "+" or a[i] == "-":
            vmf = i
        if a[i] == "=":
            sms = i

    one = []
    two = []
    three = []

    for i in range(0, vmf-1):
        one.append(a[i])

    for i in range(vmf + 2, sms - 1):
        two.append(a[i])

    for i in range(sms+2, len(a)):
        three.append(a[i])

    one = int(''.join(one))
    two = int(''.join(two))
    three = int(''.join(three))


    if a[vmf] == "+":
        if (one + two) == three:
            print("Case " + str(j+1) + ": YES")
        else:
            print("Case " + str(j+1) + ": NO")
    if a[vmf] == "-":
        if (one - two) == three:
            print("Case " + str(j+1) + ": YES")
        else:
            print("Case " + str(j+1) + ": NO")