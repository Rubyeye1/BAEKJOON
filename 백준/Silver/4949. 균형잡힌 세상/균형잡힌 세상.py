import math
import sys
from collections import deque
import copy
import datetime

while True:

    L = input()
    if L == ".":
        break

    S = []

    for i in L:

        if i == "(" or i == "[":
            S.append(i)

        elif i == ")":
            if len(S) != 0 and S[-1] == "(":
                S.pop()
            else:
                S.append(")")
                break

        elif i == "]":
            if len(S) != 0 and S[-1] == "[":
                S.pop()
            else:
                S.append("]")
                break

    if len(S) == 0:
        print('yes')
    else:
        print('no')