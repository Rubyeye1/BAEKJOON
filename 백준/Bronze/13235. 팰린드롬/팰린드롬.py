import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

L = input()

if L == L[::-1]:
    print("true")
else:
    print("false")