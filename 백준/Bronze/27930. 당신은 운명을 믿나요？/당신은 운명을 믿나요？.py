import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

L = input()
L = list(L)

K = ["K","O","R","E","A"]
Y = ["Y","O","N","S","E","I"]

Ktemp = 0
Ytemp = 0

for i in range(len(L)):

    if L[i] == K[Ktemp] and L[i] == Y[Ytemp]:
        Ktemp += 1
        Ytemp += 1
    elif L[i] == K[Ktemp]:
        Ktemp += 1
    elif L[i] == Y[Ytemp]:
        Ytemp += 1

    if Ktemp == 5:
        for j in range(len(K)):
            print(K[j], end="")
        break

    if Ytemp == 6:
        for j in range(len(Y)):
            print(Y[j], end="")
        break