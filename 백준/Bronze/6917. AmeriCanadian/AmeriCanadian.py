import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

while True:

    T = input()
    if T == "quit!":
        break

    if len(T) >= 4 and "or" in T and T[-3] != "a" and T[-3] != "e" and T[-3] != "i" and T[-3] != "o" and T[-3] != "u":
        T = T.replace("or", "our")

    print(T)