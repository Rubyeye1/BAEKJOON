import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

A = int(input(), 2)
B = int(input(), 2)
N = 100000
M = 2 ** N - 1

print(bin(A & B)[2:].zfill(N))
print(bin(A | B)[2:].zfill(N))
print(bin(A ^ B)[2:].zfill(N))
print(bin(A ^ M)[2:].zfill(N))
print(bin(B ^ M)[2:].zfill(N))