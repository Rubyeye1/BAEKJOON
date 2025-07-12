import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

N = input()

if N[-2] + N[-1] == "10":  
    print(int(N[:-2]) + 10)
else:
    print(int(N[:-1]) + int(N[-1]))