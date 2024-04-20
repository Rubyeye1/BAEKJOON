import math
import sys
from collections import deque
import copy
import datetime

while True:
    try:
        S = input()
        S = list(S)
        UpperCount = 0
        LowerCount = 0
        BlankCount = 0
        NumberCount = 0
        for i in range(len(S)):

            if S[i].isupper():
                UpperCount += 1
            elif S[i].islower():
                LowerCount += 1
            elif S[i].isdigit():
                BlankCount += 1
            else:
                NumberCount += 1

        print(LowerCount, UpperCount, BlankCount, NumberCount)
    except EOFError:
        break