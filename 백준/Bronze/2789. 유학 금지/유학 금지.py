import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

L = input()
temp = "CAMBRIDGE"

for i in range(len(temp)):
    L = L.replace(temp[i],"")

print(L)