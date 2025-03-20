import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

L = input()
temp = 0

for i in range(len(L)):
    if L[i] == 'a':
        temp += 1
    elif L[i] == 'b':
        temp += 2
    elif L[i] == 'c':
        temp += 3
    elif L[i] == 'd':
        temp += 4
    elif L[i] == 'e':
        temp += 5
    elif L[i] == 'f':
        temp += 6
    elif L[i] == 'g':
        temp += 7
    elif L[i] == 'h':
        temp += 8
    elif L[i] == 'i':
        temp += 9
    elif L[i] == 'j':
        temp += 10
    elif L[i] == 'k':
        temp += 11
    elif L[i] == 'l':
        temp += 12
    elif L[i] == 'm':
        temp += 13
    elif L[i] == 'n':
        temp += 14
    elif L[i] == 'o':
        temp += 15
    elif L[i] == 'p':
        temp += 16
    elif L[i] == 'q':
        temp += 17
    elif L[i] == 'r':
        temp += 18
    elif L[i] == 's':
        temp += 19
    elif L[i] == 't':
        temp += 20
    elif L[i] == 'u':
        temp += 21
    elif L[i] == 'v':
        temp += 22
    elif L[i] == 'w':
        temp += 23
    elif L[i] == 'x':
        temp += 24
    elif L[i] == 'y':
        temp += 25
    elif L[i] == 'z':
        temp += 26
    elif L[i] == 'A':
        temp += 27
    elif L[i] == 'B':
        temp += 28
    elif L[i] == 'C':
        temp += 29
    elif L[i] == 'D':
        temp += 30
    elif L[i] == 'E':
        temp += 31
    elif L[i] == 'F':
        temp += 32
    elif L[i] == 'G':
        temp += 33
    elif L[i] == 'H':
        temp += 34
    elif L[i] == 'I':
        temp += 35
    elif L[i] == 'J':
        temp += 36
    elif L[i] == 'K':
        temp += 37
    elif L[i] == 'L':
        temp += 38
    elif L[i] == 'M':
        temp += 39
    elif L[i] == 'N':
        temp += 40
    elif L[i] == 'O':
        temp += 41
    elif L[i] == 'P':
        temp += 42
    elif L[i] == 'Q':
        temp += 43
    elif L[i] == 'R':
        temp += 44
    elif L[i] == 'S':
        temp += 45
    elif L[i] == 'T':
        temp += 46
    elif L[i] == 'U':
        temp += 47
    elif L[i] == 'V':
        temp += 48
    elif L[i] == 'W':
        temp += 49
    elif L[i] == 'X':
        temp += 50
    elif L[i] == 'Y':
        temp += 51
    elif L[i] == 'Z':
        temp += 52

chk = 0

for i in range(2, int(temp ** 0.5) + 1):
    if temp % i == 0:
        chk = 1
        break

if chk == 1:
    print("It is not a prime word.") 
else:
    print("It is a prime word.")