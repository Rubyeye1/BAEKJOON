import math
import sys
from collections import deque
import copy
import datetime


def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fibonacci(n):
    return n-2

n = int(sys.stdin.readline())
print(fib(n), fibonacci(n))