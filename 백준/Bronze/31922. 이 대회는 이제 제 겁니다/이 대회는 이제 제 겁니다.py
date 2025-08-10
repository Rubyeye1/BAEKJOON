import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

A, P, C = map(int, sys.stdin.readline().split())

print(max(A + C, P))