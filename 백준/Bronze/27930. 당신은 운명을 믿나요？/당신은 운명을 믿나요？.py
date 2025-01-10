import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

L = input()
L = list(L)

K = []
Y = []

for i in range(len(L)):

    if L[i] == "K" and "K" not in K:
        K.append(L[i])
    if L[i] == "Y" and "Y" not in Y:
        Y.append(L[i])

    if L[i] == "O":
        if "K" in K and "O" not in K:
            K.append(L[i])
        elif "Y" in Y and "O" not in Y:
            Y.append(L[i])

    if L[i] == "N" and "O" in Y and "N" not in Y:
        Y.append(L[i])

    if L[i] == "R" and "O" in K and "R" not in K:
        K.append(L[i])

    if L[i] == "S" and "N" in Y and "S" not in Y:
        Y.append(L[i])

    if L[i] == "E":
        if "R" in K and "E" not in K:
            K.append(L[i])
        elif "S" in Y and "E" not in Y:
            Y.append(L[i])

    if L[i] == "I" and "E" in Y and "I" not in Y:
        Y.append(L[i])

    if L[i] == "A" and "E" in K and "A" not in K:
        K.append(L[i])

    if len(Y) == 6:
        for j in range(len(Y)):
            print(Y[j], end="")
        break
    elif len(K) == 5:
        for j in range(len(K)):
            print(K[j], end="")
        break
