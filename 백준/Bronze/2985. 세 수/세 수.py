import math
import sys
from collections import deque
import copy
import datetime
from datetime import date, datetime


a, b, c = map(int, sys.stdin.readline().split())

if (a + b) == c:
    a = str(a)
    b = str(b)
    c = str(c)
    print(a + "+" + b + "=" + c)
    
elif (b + c) == a:
    a = str(a)
    b = str(b)
    c = str(c)
    print(a + "=" + b + "+" + c)
    
elif (a - b) == c:
    a = str(a)
    b = str(b)
    c = str(c)
    print(a + "-" + b + "=" + c)
    
elif (b - c) == a:
    a = str(a)
    b = str(b)
    c = str(c)
    print(a + "=" + b + "-" + c)
    
elif (a * b) == c:
    a = str(a)
    b = str(b)
    c = str(c)
    print(a + "*" + b + "=" + c)
    
elif (b * c) == a:
    a = str(a)
    b = str(b)
    c = str(c)
    print(a + "=" + b + "*" + c)
    
elif (a / b) == c:
    a = str(a)
    b = str(b)
    c = str(c)
    print(a + "/" + b + "=" + c)
    
elif (b / c) == a:
    a = str(a)
    b = str(b)
    c = str(c)
    print(a + "=" + b + "/" + c)