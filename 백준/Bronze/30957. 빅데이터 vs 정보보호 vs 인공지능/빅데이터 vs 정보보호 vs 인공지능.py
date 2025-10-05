import sys
from collections import deque
import copy
import datetime
from datetime import date, datetime
import re
import math

N = int(sys.stdin.readline())
B = 0
S = 0
A = 0

temp = input()

for i in temp:
    if i == "B":
        B += 1
    elif i == "S":
        S += 1
    elif i == "A":
        A += 1

if B == S and S == A and B == A:
    print("SCU")
else:
    if B == max(B, S, A):
        print("B", end="")
    if S == max(B, S, A):
        print("S", end="")
    if A == max(B, S, A):
        print("A", end="")