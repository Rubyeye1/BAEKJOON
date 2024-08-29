import math
import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

T = int(sys.stdin.readline())

for _ in range(T):

    a = input()
    a = list(a)

    i = 0

    while True:

        if i == len(a):
            break

        if a[i].isupper():
            a.insert(i, "_")
            i += 1

        i += 1


    result = []

    for i in a:
        result.append(i.lower())

    if result[0] != "_":
        for i in range(len(result)):
            print(result[i],end="")
        print("")
    else:
        for i in range(1,len(result)):
            print(result[i],end="")
        print("")