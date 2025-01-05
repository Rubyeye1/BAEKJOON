import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

while True:

    L = input()

    if L == "#":
        break

    L = list(L)
    result = 0

    for i in range(len(L)):

        if L[i] == "A":
            result += (i+1) * 1
        elif L[i] == "B":
            result += (i+1) * 2
        elif L[i] == "C":
            result += (i+1) * 3
        elif L[i] == "D":
            result += (i+1) * 4
        elif L[i] == "E":
            result += (i+1) * 5
        elif L[i] == "F":
            result += (i+1) * 6
        elif L[i] == "G":
            result += (i+1) * 7
        elif L[i] == "H":
            result += (i+1) * 8
        elif L[i] == "I":
            result += (i+1) * 9
        elif L[i] == "J":
            result += (i+1) * 10
        elif L[i] == "K":
            result += (i+1) * 11
        elif L[i] == "L":
            result += (i+1) * 12
        elif L[i] == "M":
            result += (i+1) * 13
        elif L[i] == "N":
            result += (i+1) * 14
        elif L[i] == "O":
            result += (i+1) * 15
        elif L[i] == "P":
            result += (i+1) * 16
        elif L[i] == "Q":
            result += (i+1) * 17
        elif L[i] == "R":
            result += (i+1) * 18
        elif L[i] == "S":
            result += (i+1) * 19
        elif L[i] == "T":
            result += (i+1) * 20
        elif L[i] == "U":
            result += (i+1) * 21
        elif L[i] == "V":
            result += (i+1) * 22
        elif L[i] == "W":
            result += (i+1) * 23
        elif L[i] == "X":
            result += (i+1) * 24
        elif L[i] == "Y":
            result += (i+1) * 25
        elif L[i] == "Z":
            result += (i+1) * 26

    print(result)