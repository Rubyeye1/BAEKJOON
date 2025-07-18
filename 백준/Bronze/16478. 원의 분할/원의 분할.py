import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

Pab, Pbc, Pcd = map(int, sys.stdin.readline().split())

Pad = Pab * Pcd / Pbc

if Pab == Pcd and Pcd == Pbc:
   Pad = int(Pad)

print(Pad)