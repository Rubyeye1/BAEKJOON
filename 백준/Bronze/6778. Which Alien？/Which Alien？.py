import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

antenna = int(sys.stdin.readline())
eyes = int(sys.stdin.readline())

if antenna >= 3 and eyes <= 4:
    print("TroyMartian")

if antenna <= 6 and eyes >= 2:
    print("VladSaturnian")
    
if antenna <= 2 and eyes <= 3:
    print("GraemeMercurian")