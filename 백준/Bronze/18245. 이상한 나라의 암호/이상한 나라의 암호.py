import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

temp = 1

while True:
  L = input()

  if L == 'Was it a cat I saw?':
    break
  
  print(L[::temp+1])
  temp += 1