import math
import sys
from collections import deque
import copy
import datetime

N = int(sys.stdin.readline())

a = input()
b = input()

if (N % 2) == 1:

    for i in range(len(a)):

        if a[i] == b[i]:
            print("Deletion failed")
            break

        if i == (len(a) - 1):
            print("Deletion succeeded")

else:

    for i in range(len(a)):

        if a[i] != b[i]:
            print("Deletion failed")
            break

        if i == (len(a) - 1):
            print("Deletion succeeded")