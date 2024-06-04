import math
import sys
from collections import deque
import copy
import datetime

while True:
    
    L = input()
    if L == "EOI":
        break

    L = L.lower()

    if "nemo" in L:
        print("Found")
    else:
        print("Missing")