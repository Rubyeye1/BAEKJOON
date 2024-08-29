import math
import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

a = input()
L = []

for i in range(len(a)):
    if a[i] != " ":
        L.append(a[i])

if L[1] == L[2] and L[3] == L[4]:
    print(L[0] + L[1] + "\'" + L[3] + "\'" + L[5])
elif L[1] == L[2] and L[3] != L[4]:
    print(L[0] + L[1] + "\'" + L[3] + L[4] + L[5])
elif L[1] != L[2] and L[3] == L[4]:
    print(L[0] + L[1] + L[2] + L[3] + "\'" + L[5])
else:
    print(L[0] + L[1] + L[2] + L[3] + L[4] + L[5])