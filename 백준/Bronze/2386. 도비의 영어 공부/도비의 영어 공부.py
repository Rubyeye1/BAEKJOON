import math
import sys
from collections import deque
import copy
import datetime

while True:
    tempL = input()
    if tempL[0] == "#":
        break
    tempL = deque(tempL)
    munja = tempL.popleft()
    tempL.popleft()
    tempL = list(tempL)
    for i in range(len(tempL)):
        tempL[i] = tempL[i].lower()
    result = tempL.count(munja)
    print(munja, result)